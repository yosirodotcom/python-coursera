package com.google.tflite.imageclassification.sample.tflite

import android.content.res.AssetManager
import android.graphics.Bitmap
import android.os.SystemClock
import android.util.Log
import org.tensorflow.lite.Interpreter
import java.io.FileInputStream
import java.nio.ByteBuffer
import java.nio.ByteOrder
import java.nio.MappedByteBuffer
import java.nio.channels.FileChannel
import java.util.*
import kotlin.experimental.and

// for modelPath and labelPath please see recent version in https://www.tensorflow.org/lite/guide/hosted_models
class Classifier(assetManager: AssetManager, modelPath: String, labelPath: String, inputSize: Int) {
    private var INTERPRETER: Interpreter
    private var LABEL_LIST: List<String>
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
    ) {
        override fun toString(): String {
            return "Title = $title, Confidence = $confidence)"
        }
    }

    /**
     * Step #1 : Set the Interpreter's Options
     */
    init {
        val tfliteOptions = Interpreter.Options() // #1.a.
        tfliteOptions.setNumThreads(5) // #1.b.
        tfliteOptions.setUseNNAPI(true) // #1.c.
        INTERPRETER = Interpreter(loadModelFile(assetManager, modelPath),tfliteOptions) //#2.e. initializing the interpreter
        LABEL_LIST = loadLabelList(assetManager, labelPath) //#2.d. load the labels
    }

    /**
     * Step #2 : Loading model and label file into the interpreter
     */
    private fun loadModelFile(assetManager: AssetManager, modelPath: String): MappedByteBuffer {
        // #2.a. get the file descriptor of the model
        val fileDescriptor = assetManager.openFd(modelPath)
        // #2.b. read the model file's channels
        val inputStream = FileInputStream(fileDescriptor.fileDescriptor)
        val fileChannel = inputStream.channel
        val startOffset = fileDescriptor.startOffset
        val declaredLength = fileDescriptor.declaredLength
        // #2.c. load the TFLite model as
        return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength)
    }

    private fun loadLabelList(assetManager: AssetManager, labelPath: String): List<String> {
        return assetManager.open(labelPath).bufferedReader().useLines { it.toList() }

    }

    /**
     * Continue from Camera2BasicFragment.kt for Part #3
     */
    fun recognizeImage(bitmap: Bitmap): List<Recognition> {
        val scaledBitmap = Bitmap.createScaledBitmap(bitmap, INPUT_SIZE, INPUT_SIZE, false) //3.d. resize the bitmap to 224x224
        val byteBuffer = convertBitmapToByteBuffer(scaledBitmap)

        /**
         * Step #4: Perform Inference
         * Pass input to the interpreter and invoke the interpreter
         */
        val result = Array(1) { ByteArray(LABEL_LIST.size) }
        INTERPRETER.run(byteBuffer, result)
        return getSortedResult(result)
    }


    private fun addPixelValue(byteBuffer: ByteBuffer, intValue: Int): ByteBuffer {

        byteBuffer.put((intValue.shr(16) and 0xFF).toByte()) //3.f
        byteBuffer.put((intValue.shr(8) and 0xFF).toByte()) //3.f
        byteBuffer.put((intValue and 0xFF).toByte()) //3.f
        return byteBuffer
    }

    /** Writes Image data into a `ByteBuffer`.  */
    private fun convertBitmapToByteBuffer(bitmap: Bitmap): ByteBuffer {
        val imgData = ByteBuffer.allocateDirect(INPUT_SIZE * INPUT_SIZE * PIXEL_SIZE) //3.e. Convert bitmap to bytebuffer (batch size is 1 (quatized model))
        imgData.order(ByteOrder.nativeOrder()) //3.e.
        val intValues = IntArray(INPUT_SIZE * INPUT_SIZE)


        imgData.rewind()
        bitmap.getPixels(intValues, 0, bitmap.width, 0, 0, bitmap.width, bitmap.height)
        // Convert the image to floating point.
        var pixel = 0
        val startTime = SystemClock.uptimeMillis()
        for (i in 0 until INPUT_SIZE) {
            for (j in 0 until INPUT_SIZE) {
                val `val` = intValues[pixel++]
                addPixelValue(imgData, `val`)
            }
        }
        return imgData;
//        val endTime = SystemClock.uptimeMillis()
//        LOGGER.v("Timecost to put values into ByteBuffer: " + (endTime - startTime))
    }

    /**
     * Step #5: Obtain and Map Results
     * Map our resulting confidence values to labels
     */
    private fun getSortedResult(labelProbArray: Array<ByteArray>): List<Recognition> {
        Log.d("Classifier", "List Size:(%d, %d, %d)".format(labelProbArray.size, labelProbArray[0].size, LABEL_LIST.size))
        // Here we instantiate a queue to accumulate the results with its size
        // indicating the number of results to be shown
        val pq = PriorityQueue(
                MAX_RESULTS,
                Comparator<Recognition> { (_, _, confidence1), (_, _, confidence2)
                    ->
                    java.lang.Float.compare(confidence1, confidence2) * -1
                })
        // We assume the minimum score value to be THRESHOLD=40% or above
        // for a result to be considered as a recognition
        for (i in LABEL_LIST.indices) {
            val confidence = labelProbArray[0][i]
            if (confidence >= THRESHOLD) {
                Log.d("confidence value:", "" + confidence);
                pq.add(Recognition("" + i,
                        if (LABEL_LIST.size > i) LABEL_LIST[i] else "Unknown",
                        ((confidence).toFloat() / 255.0f)
                ))
            }
        }
        Log.d("Classifier", "pqsize:(%d)".format(pq.size))

        val recognitions = ArrayList<Recognition>()
        val recognitionsSize = Math.min(pq.size, MAX_RESULTS)
        for (i in 0 until recognitionsSize) {
            recognitions.add(pq.poll())
        }
        return recognitions
    }

}