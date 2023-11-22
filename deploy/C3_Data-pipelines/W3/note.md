# Using an iterator to navigate

> dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4])
> it = iter(dataset)
> 
> while True:
>     try:
>         print(next(it))
>     except StopIteration as e:
>         break
> 
> tf.Tensor(1, shape=(), dtype=int32)
> tf.Tensor(2, shape=(), dtype=int32)
> tf.Tensor(3, shape=(), dtype=int32)
> tf.Tensor(4, shape=(), dtype=int32)

# Loading numpy arrays (from_tensor_slices)

> (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
> dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))

> for image, label in tfds.as_numpy(dataset.take(2)):
>     print(image.shape, label)

- Output:
    (32, 32, 3)[6]
    (32, 32, 3)[9]


# Specifying data types
- defaults to a tf.float32 scalar
> numeric_features_column = tf.feature_column.numeric_column(key="SepalLength") 
- represent a tf.float64 scalar
> numeric_features_column = tf.feature_column.numeric_column(key="SepalLength", dtype=tf.float64) 

# Shapes for different numeric data
- represent a 10-element vector in which each cell contains a tf.float32
> vector_feature_column = tf.reature_column.numeric_column(key='Bowling', shape=10)
- represent a 10x5 matrix in which each cell contains a tf.float32
> matrix_feature_column = tf.feature_column.numeric_column(key="MyMatrix", shape=[10,5])

# Bucketizing features
- first, convert the raw input to a numeric column
> numeric_feature_column = tf.feature_column.numeric_column("Year")
- then, bucketize the numeric column on the years 1960, 1980, and 2000
> buketized_feature_column = tf.feature_column.bucketized_column(
>     source_column = numeric_feature_column,
>     boundaries = [1960, 1980, 2000]
> )

# Categorizing identity features
> identity_feature_column = tf.feature_column.categorical_column_with_identity(
>     key='my_feature_b',
>     num_buckets=4 # values [0,4]
> )

Here is the example code that calls tf.feature_column.categorical_column_with_identity to implement a categorical identity column. 
Create categorical output for an integer feature named "my_feature_b".  
The values of my_feature_b must be greater than or equal to zero and less than the number of buckets.  
For the preceding call to work, the input_fn() must return a dictionary containing 'my_feature_b' as a key. 
The values assigned to 'my_feature_b' must belong to the set of numbers from 0 to 4, excluding 4. 

# Creating a categorical vocab column
- from a vocabulary list
> vocabulary_feature_column = tf.feature_column.categorical_column_with_vocabulary_list(
>     key=feature_name, 
>     vocabulary_list=["kitchenware", "electronics", "sports"]
> )
- from a vocabulary file
> vocabulary_feature_column = tf.feature_column.categorical_column_with_vocabulary_file(
>     key=feature_name,
>     vocabulary_file="product_class.txt",
>     vocabulary_size=3
> )

# Hashed column
A common technique used when there are many categories is to hash them to a smaller set. you do not need to provide the vocabulary, and you can choose to make the number of hash buckets significantly smaller than the number of actual categories to save space.

> hashed_feature_column = tf.feature_column.categorical_column_with_hash_bucket(
>     key="some_feature",
>     hash_bucket_size=100 # the number of categories
> )

# Crossed column
Feature crosses are synthetic featured formed by multiplying (or crossing) two or more features. Crossing features can provide predictive abilities beyond what those features could provide individually. 

- Bucketize the latitude and longitude using the 'edges'
> latitude_bucket_fc = tf.feature_column.bucketized_column(> 
>     tf.feature_column.numeric_column('latitude')
>     list(atlanta.latitude.edges)
> )

> longitude_bucket_fc = tf.feature_column.bucketized_column(
>     tf.feture_column.numeric_column('longitude'),
>    list(atlanta.longitude.edges)
> )

- Cross the bucketized columns, using 5000 hash bins.
> crossed_lat_lon_fc = tf.feature_column.crossed_column(
>     [latitude_bucket_fc, longitude_bucket_fc], 5000
> )

# Embedding Column
One downside with one hot encoded vectors above is that they can lead to some very large sparse and inefficient vectors embedding columns work very well to avoid this.

> embedding_dimensions = number_of_categories**0.25
> categorical_column = . . . # create any categorical column

Represent the categorical column as an embedding column. This means createing an embedding vector lookup table with one element for each category.

> embedding_column = tf.feature_column.embedding_column(
>     categorical_column=categorical_column,
>     dimension=embedding_dimensions
> )

# Extracting and Loading Data to Pipelines

- Loading a dataset from npz (numpy)
Download dataset
> DATA_URL = 'https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz'
> path = tf.keras.utils.get_file('mnist.npz', DATA_URL) 
Extract train and test examples
> with np.load(path) as data:
>   train_examples = data['x_train']
>   train_labels = data['y_train]
>   test_examples = data['x_test']
Create train and test datasets out of the examples
> train_dataset = tf.data.Dataset.from_tensor_slices((train_examples, train_labels))
> test_dataset = tf.data.Dataset.from_tensor_slices(test_examples)
> 
> for feat, targ in train_dataset.take(2):
>   print('Features shape: {}, Target: {}'.format(feat.shape, targ))

Expected Output:
    Features shape: (28, 28), Target: 5
    Features shape: (28, 28), Target: 0

- Create DataFrames out of CSVs
> csv_file = tf.keras.utils.get_file('heart.csv', 'https://storage.googleapis.com/applied-dl/heart.csv')
> df = pd.read_csv(csv_file)
> df.head()

- Loading the structured dataset
> TRAIN_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
> train_file_path = tf.keras.utils.get_file("train.csv", TRAIN_DATA_URL)
> 
> df = pd.read_csv(train_file_path, sep=',')

- Numeric column
> NUMERIC_FEATURES = ["age", "n_siblings_spouses", "parch", "fare"]
> dense_df = df[NUMERIC_FEATURES]
> 
> numeric_columns = []
> for feature in NUMERIC_FEATURES:
>   num_col = tf.feature_column.numeric_column(feature)
>   numeric_columns.append(tf.feature_column.indicator_column(num_col))
> 
- Categorical column
> CATEGORIES = {
>    'sex': ['male', 'female'],
>    'class':['First', 'Second', 'Third'],
>    'deck': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
>    'embark_town': ['Cherbourg', 'Southhampton', 'Queenstown'],
>    'alone': ['y', 'n']
>}
> cat_df = df[list(CATEGORIES.keys())]
> 
> categorical_columns =[]
> 
> for feature, vocab in CATEGORIES.items():
>     cat_col = tf.feature_column.categorical_column_with_vocabulary_list(
>         key=feature,
>         vocabulary_list=vocab
>     )
>     categorical_columns.append(tf.feature_column.indicator_column(cat_col))


- Discretizing features
I can set my frame for foul to be categorical, and change it into codes, and then have it mapped to pointers of values instead of just the raw values, as you can see here. File has changed to 234, et cetera, instead of just strings describing it.
> df['thal'] = pd.Categorical(df['thal'])
> df['thal'] = df.thal.cat.codes
> df.head()

- Dataset from features and targets
> target = df.pop('target')
> dataset = tf.data.Dataset.from_tensor_slices((df.values, target.values))
> 
> for feat, targ in dataset.take(5):
>   print ('Features: {}, Target: {}'.format(feat, targ))

Expected Output:
    Features: [63.  1.  1.  145.  233.  1.  2.  150.  0.  2.3  3.  0.  2. ], Target: 0
    . . . 

- Download and extract images
> import pathlib
> 
> DATA_URL = 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'
> data_root_orig = tf.keras.utils.get_file(origin=DATA_URL, fname='flower_photos', untar=True)
> data_root = pathlib.Path(data_root_orig)
> 
> label_names = sorted(item.name for item in data_root.glob('*/) if item.is_dir()) # membuat list nama-nama dari sub directories yang menampung gambar-gambar. nama subdirectories merupakan label

- Display a random sample from the loaded dataset
> import random
> import IPython.display as display
> 
> all_image_paths = list(data_root.glob('*/*'))
> all_image_paths = [str(path) for path in all_image_paths]
> random.shuffle(all_image_paths)
> 
> image_count = len(all_image_paths)
> 
> image_path = random.choice(all_image_paths)
> display.display(display.Image(image_path))
> 

- Loading Texts

> DIRECTORY_URL = "https://storage.googleapis.com/download.tensorflow.org/data/illiad/"
> FILE_NAME = "cowper.txt"
> file_path = tf.keras.utils.get_file(
>     name,
>     origin=DIRECTORY_URL + FILE_NAME
> )
> lines_dataset = tf.data.TextLineDataset(file_path)
> for text_data in tfds.as_numpy(lines_dataset.take(3)):
>     print(text_data.decode('utf-8'))

- Loading TFRecord files
But what if you have too much data to having a single file or archive and that you might have to stream it all over network. Well, in this case, TF Record is your friend. 
> filenames = [tf_record_filename]
> raw_dataset = tf.dataTFRecordDataset(filenames)
> 
> feature_description = {
>     "feature1": tf.io.FixedLenFeature((), tf.string),
>     "feature2": tf.io.FixedLenFeature((), tf.int64),
> }
> 
> for raw_record in raw_dataset.take(1):
>     example = tf.io.parse_single_example(raw_record, feature_description)
>     print(example)

- Image Folder Generator
> def make_generator():
>     train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
>         rescale=1. / 255,
>         rotation_range=20,
>         zoom_range=[0.8, 1.2]
>     )
>     train_generator = train_datagen.flow_from_directory(
>         catsdogs,
>         target_size=(224, 224),
>         class_mode='categorical',
>         batch_size=32
>     )
>     return train_generator
> 
> train_generator = tf.data.Dataset.from_generator(
>     make_generator,
>     (tf.float32, tf.uint8)
> )






