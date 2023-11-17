package com.google.tflite.catvsdog.tflite

import android.content.res.AssetManager
import android.graphics.Bitmap
import android.util.Log
import org.tensorflow.lite.Interpreter
import java.io.FileInputStream
import java.nio.ByteBuffer
import java.nio.ByteOrder
import java.nio.MappedByteBuffer
import java.nio.channels.FileChannel
import java.util.*



class Classifier(assetManager: AssetManager, modelPath: String, labelPath: String, inputSize: Int) {
    private var interpreter: Interpreter
    private var lableList: List<String>
    private val INPUT_SIZE: Int = inputSize
    private val PIXEL_SIZE: Int = 3
    private val IMAGE_MEAN = 0
    private val IMAGE_STD = 255.0f
    private val MAX_RESULTS = 3
    private val THRESHOLD = 0.4f

    data class Recognition(
        var id: String = "",
        var title: String = "",
        var confidence: Float = 0F
    )  {
        override fun toString(): String {
            return "Title = $title, Confidence = $confidence)"
        }
    }

    /**
    #1 Initiate the Interpreter

    Set the Interpreter's Options

    Options: A class for controlling runtime interpreter behaviour
    - setNumThreads(int numThreads)
    - setUseNNAPI(boolean useNNAPI)
    - setAllowFp16PrecisionForFp32(boolean allow) // One cool feature is that you can use mixed Precision calculation in your models when possible
    - addDelegate(Delegate delegate) // you could instruct The Interpreter to add a delegate to utilize the GPU if it's available

   Setting the interpreters options is one of the preliminary steps to get started with using it.
   This is entirely optional as a TF Lite model can be loaded without setting these options and
   The Interpreter will just use the defaults, but I think it's good to know what the options are.

   The various options allow you to change the number of threads that The Interpreter will use for
   inference with a set number of threads call. You can then leverage the neural network API to
   enable Hardware acceleration on your device where it's available.
   */

    init {
        val options = Interpreter.Options()
        options.setNumThreads(5)
        options.setUseNNAPI(true)
        interpreter = Interpreter(loadModelFile(assetManager, modelPath), options) // 1.a. Once we have the model, it's then simple to instantiate The Interpreter by passing it the model and the options like this.
        lableList = loadLabelList(assetManager, labelPath)
    }

    /** 1.b. Loading the model and labels wit loadModelFile function */

    private fun loadModelFile(assetManager: AssetManager, modelPath: String): MappedByteBuffer {
        val fileDescriptor = assetManager.openFd(modelPath) // loading the model the TF light file that you created when used an Android should be placed in the assets folder. You can load resources from here using the asset manager as shown to get a file descriptor.
        val inputStream = FileInputStream(fileDescriptor.fileDescriptor) // The file descriptor is then passed to a file input stream object in order to set up an put stream.
        //
        /*
        The file will be loaded into a file Channel which needs the input stream as well as the
        star offset and declared length of the file
         */
        val fileChannel = inputStream.channel
        val startOffset = fileDescriptor.startOffset
        val declaredLength = fileDescriptor.declaredLength
        //
        return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength) //and to get the model representation. We then map that file channel to read in the raw bytes of the model.
    }

    private fun loadLabelList(assetManager: AssetManager, labelPath: String): List<String> {
        return assetManager.open(labelPath).bufferedReader().useLines { it.toList() }

    }

    /**
     * Returns the result after running the recognition with the help of interpreter
     * on the passed bitmap
     */

    /**
    #2 Preparing the Image Input
    Input image pixel buffer is converted to the format recognized by the model:
    */

    /**
    #3 Perform Inference
    Pass input to the Interpreter and Invoke the Interpreter:
     */

    fun recognizeImage(bitmap: Bitmap): List<Recognition> {
        val scaledBitmap = Bitmap.createScaledBitmap(bitmap, INPUT_SIZE, INPUT_SIZE, false) // 2a. Resize the bitmap to 224 x 224
        val byteBuffer = convertBitmapToByteBuffer(scaledBitmap)
        val result = Array(1) { FloatArray(lableList.size) } // 3a. running inference and accumulating the result
        interpreter.run(byteBuffer, result)
        return getSortedResult(result)
    }


    private fun convertBitmapToByteBuffer(bitmap: Bitmap): ByteBuffer {
        val byteBuffer = ByteBuffer.allocateDirect(4 * INPUT_SIZE * INPUT_SIZE * PIXEL_SIZE) // 2b. Convert bitmap to bytebuffer. Batch size is 4 (Floating point model)
        byteBuffer.order(ByteOrder.nativeOrder())
        val intValues = IntArray(INPUT_SIZE * INPUT_SIZE)

        bitmap.getPixels(intValues, 0, bitmap.width, 0, 0, bitmap.width, bitmap.height)
        var pixel = 0
        // Get R-G-B channels of the image:
        for (i in 0 until INPUT_SIZE) {
            for (j in 0 until INPUT_SIZE) {
                val input = intValues[pixel++]

                byteBuffer.putFloat((((input.shr(16)  and 0xFF) - IMAGE_MEAN) / IMAGE_STD))
                byteBuffer.putFloat((((input.shr(8) and 0xFF) - IMAGE_MEAN) / IMAGE_STD))
                byteBuffer.putFloat((((input and 0xFF) - IMAGE_MEAN) / IMAGE_STD))
            }
        }
        return byteBuffer
    }

    /**
     * #4 Obtain and Map Results
     *
     * Map our resulting confidence values to labels
     * Remember we have confidence values per class, so we might see that an image is
     * one percent dog and 99 percent cat.
     */
    private fun getSortedResult(labelProbArray: Array<FloatArray>): List<Classifier.Recognition> {
        Log.d("Classifier", "List Size:(%d, %d, %d)".format(labelProbArray.size,labelProbArray[0].size,lableList.size))

        // Here we instantiate a queue to accumulate the results with its size indicating the number
        // of results to be shown.
        // They get sorted as they're loaded into the queue, and we can then pick the top x values.
        // In the case of cats versus dogs, we'll just take the top value overall.

        val pq = PriorityQueue(
            MAX_RESULTS,
            Comparator<Classifier.Recognition> {
                    (_, _, confidence1), (_, _, confidence2)
                -> java.lang.Float.compare(confidence1, confidence2) * -1
            })

        for (i in lableList.indices) {
            val confidence = labelProbArray[0][i]
            if (confidence >= THRESHOLD) {
                pq.add(Classifier.Recognition("" + i,
                    if (lableList.size > i) lableList[i] else "Unknown", confidence)
                )
            }
        }
        Log.d("Classifier", "pqsize:(%d)".format(pq.size))

        val recognitions = ArrayList<Classifier.Recognition>()
        val recognitionsSize = Math.min(pq.size, MAX_RESULTS)
        for (i in 0 until recognitionsSize) {
            recognitions.add(pq.poll())
        }
        return recognitions
    }

}