# TFDS Dataset

What ML model you can use from this data:
- Image Data: Classification, Object Detection, Segmentation, Generation
- Structured Data: Regression, Recommendation
- Text Data: Classification, Sentiment Analysis, Generation, Question-answering
- Audio Data: Speech recognition, Music, Recommendation, Audio Segementation
- Video Data: Action recognition, Video classification, Object tracking, video understanding
- Translate: Neural machine translation, Transliteration, Unsupervised Machine, Translation

Some popular datasets in TFDS:
- Image Data: MNIST, CIFAR10, COCO2014, KITTI
- Structured Data: Titanic, IRIS, Amazon US reviews
- Text Data: Classification, IMDB reviews, Wikipedia, CNN - Daily Mail, SQuAD
- Audio Data: NSynth, Groove
- Video Data: UCF-101, Moving MNIST
- Translate: WMT, TED multi-translate


# Data Pipelines
- Data pipelines work on the principle of ETL, which stands for extract, transform, load.
- Lihat penerapannya pada C3_W1_Lab_1
- To see available datasets print(tfds.list_builders())

tfds.load('mnist', split='train')
- Now, what if you wanted to only load the train split of the dataset? You could do this by explicitly specifying the required split you wish to load by making use of the split parameter in the tfds.load API

tfds.load('mnist', with_info=True)
- To view a dataset's information pass with_info equals True into the tfds.load API

- Extracting properties from DatasetInfo:
    >>> print(info.urls)
    >>> print(info.features['image'])
    >>> print(info.features['label'])
    >>> print(info.splits['train'].num_examples)
    >>> print(info.splits['test'].num_examples)

# Versioning Datasets
- mnist = tfds.load("mnist:1.*.*")
    - first number = major version
    - second number = minor version
    - third number = patch version

tfds.load('mnist', as_supervised=True)
- If you do this with as supervised equals true, then your dataset will be preformatted into tuples of data and label as you can see here. image.shape = (1, 28, 28, 1), label.shape = (1,)
- If you set as a false, your dataset will be available as a dictionary.

- Using existing splits
    train: tfds.load(name, split=tdfs.Split.TRAIN)
    validation: tfds.load(name, split=tdfs.Split.VALIDATION)
    test: tfds.load(name, split=tdfs.Split.TEST)
    all: tfds.load(name, split=tdfs.Split.ALL)
- custom split
    tfds.load('coco2014', split=tdfs.Split('test2015))

- DatesetBuilder
    - pick dataset: mnist_builder = tfds.builder("mnist)
    - download: mnist_builder.download_and_prepare()
    - extract dataset: mnist_builder.as_dataset(split=tfds.Split.TRAIN)

- Another way to load
    data = tf.keras.datasets.fashion_mnist
    (training_images, training_labels), (test_images, test_labels) = data.load_data()
- atau
    (training_images, training_labels), (test_images, test_labels) = tfds.as_numpy(
        tfds.load(
            'fashion_mnist',
            split = ['train', 'test'],
            batch_size = 1,
            as_supervised = True
        )
    )

- Another scenario jika menggunakan batches

    data = tfds.load('horses_or_humans', split='train', as_supervised=True)

    train_batches = data.shuffle(100).batch(10)
    validation_batches = val_data.batch(32)

    model = tf.keras.models.Sequential(...)
    model.compile(...)
    history = model.fit(
        train_batches, 
        epochs=10
    ) 
- atau
    history = model.fit(
        train_batches, 
        epochs=10,
        validation_data=validation_batches,
        validation_steps=1
    ) 





