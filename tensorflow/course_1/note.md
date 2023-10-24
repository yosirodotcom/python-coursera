Perbedaan paradigma Programming dan Machine Learning:

Programming:
Input(Rules, Data) --> Output(Answer)

Machine Learning:
Output(Answer, Data) --> Output(Rules)

# Image Recognition

Pre-trained:
- Usahakan data yang akan di training dalam bentuk numeric. Jadi jika ada data text, maka bisa di konversi terlebih dahulu, apakah dengan metode dummy variable atau konversi data menjadi nominal.

Data Wrangling:
- Jika data imagenya berbentuk 255 color, maka untuk menormalisasi datanya cukup dengan membaginya dengan 255. Contoh: X_train = X_train/255

Modelling:
- Tentukan layer dengan fungsi Sequential
    - Layer ke-1: tf.keras.layers.Flatten() --> berfungsi untuk membuat data berdimensi 2 atau lebih menjadi 1 dimensi, karena pada NN, data input harus berdimensi 1.
    - Layer ke-2,3, dst nya: tf.keras.layers.Dense(128, activation=tf.nn.relu) --> Akan ada pembahasan lanjutan dalam tuning paramater dari hidden layer ini.
    - Layer terakhir : tf.keras.layers.Dense(10, activation=tf.nn.softmax) --> akan ada pembahasan lanjutan dalam tuning paramater dari output layer ini.
- Tentukan loss dan optimizer. Contoh: model.compile(optimizer=t.optimizer.Adam(), loss="sparse_categorical_crossentropy", metrics=["accuracy])
- Train model. Contoh: model.fit(X, y, epochs=100)