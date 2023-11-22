Merging data train and test
>>> tfds.load('mnist:3.*.*', split='train+test')

Split in data train
>>> tfds.load(mnist:3.*.*', split='train[:10000]')

or
>>> tfds.load(mnist:3.*.*', split='train[:20%]')

Split with folds
>>> val_ds = tfds.load('mnist:3.*.*', split=['train[{}%:{}%]'.format(k, k+20) for k in range(0,100,20)])
>>> train_ds = tfds.load('mnist:3.*.*', split=['train[:{}%]+train[{}%:]'.format(k, k+20) for k in range(0,100,20)])

Split method with the first 10% of test + the last 80% of train
>>> 10_80pct_ds = tfds.load('mnist:3.*.*', split='test[:10%]+train[-80%:]')

how to use the feature descriptions to be able to decode the binary of the TFRecords to get the data that you want. See the C3_W2_lab_2


