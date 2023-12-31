/* Copyright 2019 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

package com.google.tflite.objectdetection.tflite

import android.content.res.AssetManager
import android.graphics.Bitmap
import android.graphics.RectF
import android.os.Trace
import android.util.ArrayMap
import org.tensorflow.lite.Interpreter
import com.google.tflite.objectdetection.env.Logger
import java.io.*
import java.nio.ByteBuffer
import java.nio.ByteOrder
import java.nio.MappedByteBuffer
import java.nio.channels.FileChannel
import java.util.*

/**
 * Wrapper for frozen detection models trained using the Tensorflow Object Detection API:
 * github.com/tensorflow/models/tree/master/research/object_detection
 */
class TFLiteObjectDetectionAPIModel private constructor() : Classifier {
    override val statString: String
        get() = TODO("not implemented") //To change initializer of created properties use File | Settings | File Templates.
    private var isModelQuantized: Boolean = false
    // Config values.
    private var inputSize: Int = 0
    // Pre-allocated buffers.
    private val labels = Vector<String>()
    private var intValues: IntArray? = null
    // outputLocations: array of shape [Batchsize, NUM_DETECTIONS,4]
    // contains the location of detected boxes
    private var outputLocations: Array<Array<FloatArray>>? = null
    // outputClasses: array of shape [Batchsize, NUM_DETECTIONS]
    // contains the classes of detected boxes
    private var outputClasses: Array<FloatArray>? = null
    // outputScores: array of shape [Batchsize, NUM_DETECTIONS]
    // contains the scores of detected boxes
    private var outputScores: Array<FloatArray>? = null
    // numDetections: array of shape [Batchsize]
    // contains the number of detected boxes
    private var numDetections: FloatArray? = null

    private var imgData: ByteBuffer? = null

    private var tfLite: Interpreter? = null

    override fun recognizeImage(bitmap: Bitmap): List<Classifier.Recognition> {
        // Log this method so that it can be analyzed with systrace.
        Trace.beginSection("recognizeImage")

        Trace.beginSection("preprocessBitmap")
        // Preprocess the image data from 0-255 int to normalized float based
        // on the provided parameters.
        bitmap.getPixels(intValues, 0, bitmap.width, 0, 0, bitmap.width, bitmap.height) //Step 6

        imgData!!.rewind()

        // Step 7
        // when we have the pixel values, we can normalize them and load them to be ready for inference.
        for (i in 0 until inputSize) {
            for (j in 0 until inputSize) {
                val pixelValue = intValues!![i * inputSize + j]
                if (isModelQuantized) {
                    // Quantized model
                    imgData!!.put((pixelValue shr 16 and 0xFF).toByte())
                    imgData!!.put((pixelValue shr 8 and 0xFF).toByte())
                    imgData!!.put((pixelValue and 0xFF).toByte())
                } else { // Float model
                    imgData!!.putFloat(((pixelValue shr 16 and 0xFF) - IMAGE_MEAN) / IMAGE_STD)
                    imgData!!.putFloat(((pixelValue shr 8 and 0xFF) - IMAGE_MEAN) / IMAGE_STD)
                    imgData!!.putFloat(((pixelValue and 0xFF) - IMAGE_MEAN) / IMAGE_STD)
                }
            }
        } //end Step 7
        Trace.endSection() // preprocessBitmap

        // Step 8 Pull out the tensor output
        // Copy the input data into TensorFlow.
        // Since we know that the model generates four outputs will need for arrays to hold the results. 
        // And here's the code for that. The first three arrays are all an array containing an array of the 
        // number of detections. The last array is an array holding a single value which contains 
        // the number of detections. The reason why it's arrays holding array's values is that this is the 
        // data structure that most closely resembles a tensor.
        Trace.beginSection("feed")
        outputLocations = Array(1) { Array(NUM_DETECTIONS) { FloatArray(4) } }
        outputClasses = Array(1) { FloatArray(NUM_DETECTIONS) }
        outputScores = Array(1) { FloatArray(NUM_DETECTIONS) }
        numDetections = FloatArray(1)
        // So in order to do the inference, we'll create the input array from the image data and will 
        // create the structure for the outputs as a hashmap with the key being the index and the value 
        // being the appropriate structure for that element in the output that you saw on the last slide. 
        // Well, then invoke the TF lite interpreter with the run for multiple inputs and outputs passing 
        // it the input array and this output map. 
        val inputArray = arrayOf<Any>(imgData!!)
        val outputMap = ArrayMap<Int, Any>()
        outputMap[0] = outputLocations!!
        outputMap[1] = outputClasses!!
        outputMap[2] = outputScores!!
        outputMap[3] = numDetections!!
        // end Step 8
        Trace.endSection()

        // Run the inference call.
        Trace.beginSection("run")
        tfLite!!.runForMultipleInputsOutputs(inputArray, outputMap)
        Trace.endSection()

        // Show the best detections.
        // after scaling them back to the input size.
        // Step 8
        // So it's time to map them to the screen UI drawing the bounding boxes and the labels.
        val recognitions = ArrayList<Classifier.Recognition>(NUM_DETECTIONS)
        for (i in 0 until NUM_DETECTIONS) {
            // First, we need to detect the coordinates for the bounding rectangle, 
            // and second detect the label and confidence for the object within it. 
            // This code parses the output locations tensor to turn it into a rectangle. 
            // The eye indicates the current detection. The rectangle in Android takes four 
            // parameters for left top right and bottom. The model returns top left bottom and 
            // right so we have to do them slightly out of order as you can see.
            val detection = RectF(
                    outputLocations!![0][i][1] * inputSize,
                    outputLocations!![0][i][0] * inputSize,
                    outputLocations!![0][i][3] * inputSize,
                    outputLocations!![0][i][2] * inputSize)
            // SSD Mobilenet V1 Model assumes class 0 is background class
            // in label file and class labels start from 1 to number_of_classes+1,
            // while outputClasses correspond to class index from 0 to number_of_classes
            val labelOffset = 1
            recognitions.add(
                // For the results labels and confidence scores, 
                // these are in output classes and output scores respectively 
                // so we can create the output string like this.
                    Classifier.Recognition(
                            "" + i,
                            labels[outputClasses!![0][i].toInt() + labelOffset],
                            outputScores!![0][i],
                            detection))
        }
        Trace.endSection() // "recognizeImage"
        return recognitions
    } 
    // end Step 8 and go to step 9 in DetectorActivity.kt

    override fun enableStatLogging(debug: Boolean) {
        //Not implemented
    }

    override fun close() {
        //Not needed.
    }

    override fun setNumThreads(numThreads: Int) {
        if (tfLite != null) tfLite!!.setNumThreads(numThreads)
    }

    override fun setUseNNAPI(isChecked: Boolean) {
        if (tfLite != null) tfLite!!.setUseNNAPI(isChecked)
    }

    companion object {
        private val LOGGER = Logger()

        // Only return this many results.
        private val NUM_DETECTIONS = 10
        // Float model
        private val IMAGE_MEAN = 128.0f
        private val IMAGE_STD = 128.0f
        // Number of threads in the java app
        private val NUM_THREADS = 4

        /** Memory-map the model file in Assets.  */
        @Throws(IOException::class)
        private fun loadModelFile(assets: AssetManager, modelFilename: String): MappedByteBuffer {
            val fileDescriptor = assets.openFd(modelFilename)
            val inputStream = FileInputStream(fileDescriptor.fileDescriptor)
            val fileChannel = inputStream.channel
            val startOffset = fileDescriptor.startOffset
            val declaredLength = fileDescriptor.declaredLength
            return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength)
        }

        /**
         * Initializes a native TensorFlow session for classifying images.
         *
         * @param assetManager The asset manager to be used to load assets.
         * @param modelFilename The filepath of the model GraphDef protocol buffer.
         * @param labelFilename The filepath of label file for classes.
         * @param inputSize The size of image input
         * @param isQuantized Boolean representing model is quantized or not
         */
        @Throws(IOException::class)
        fun create(
                assetManager: AssetManager,
                modelFilename: String,
                labelFilename: String,
                inputSize: Int,
                isQuantized: Boolean): Classifier {
            val d = TFLiteObjectDetectionAPIModel()

            var labelsInput: InputStream? = null
            val actualFilename = labelFilename.split("file:///android_asset/".toRegex())
                    .dropLastWhile { it.isEmpty() }.toTypedArray()[1]
            labelsInput = assetManager.open(actualFilename) //Step 5
            // in other approach for step 5 is:
            //labels = assetManager.open("labelmap.txt").BufferedReader().useLines{it.toList()}
            val br: BufferedReader?
            br = BufferedReader(InputStreamReader(labelsInput!!))
            while (br.readLine()?.let { d.labels.add(it) } != null);
            br.close()

            d.inputSize = inputSize

            try {
                val options = Interpreter.Options() //Step 1
                options.setNumThreads(4) //Step 2
                options.setUseNNAPI(false) //Step 3
                d.tfLite = Interpreter(loadModelFile(assetManager, modelFilename), options) //Step 4
            } catch (e: Exception) {
                throw RuntimeException(e)
            }

            d.isModelQuantized = isQuantized
            // Pre-allocate buffers.
            val numBytesPerChannel: Int
            if (isQuantized) {
                numBytesPerChannel = 1 // Quantized
            } else {
                numBytesPerChannel = 4 // Floating point
            }
            d.imgData = ByteBuffer.allocateDirect(1 * d.inputSize * d.inputSize * 3 * numBytesPerChannel)
            d.imgData!!.order(ByteOrder.nativeOrder())
            d.intValues = IntArray(d.inputSize * d.inputSize)

//            d.tfLite!!.setNumThreads(NUM_THREADS)
            d.outputLocations = Array(1) { Array(NUM_DETECTIONS) { FloatArray(4) } }
            d.outputClasses = Array(1) { FloatArray(NUM_DETECTIONS) }
            d.outputScores = Array(1) { FloatArray(NUM_DETECTIONS) }
            d.numDetections = FloatArray(1)
            return d
        }
    }
}
