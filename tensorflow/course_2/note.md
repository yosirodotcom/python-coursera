- Untuk memperkaya data image dan mengandle masalah overfitting maka kita menggunakan metode Augmentation, caranya hanya dengan menambahkan parameter pada ImageDataGenerator:

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

- Pada C2_W3_Lab_1 dijelaskan bagaimana menggunakan transfer learning. Karena layer yang begitu banyak sehingga overfitting masih saja terjadi, tapi untungnya ada metode lain untuk mengurangi masalah overfitting tersebut, yaitu regularization:dropout. Pada notebook ini juga di ajarkan bagaimana membentuk layer tanpa fungsi Sequential, sehingga bisa lebih fleksibel.

- Model pada C2_W3_Lab_1, menggunakan metode:
    - transfer learning
    - membentuk model tanpa Sequential
    - model compile
    - mengelola file image dari zip ke folder subfolder
    - menggunakan ImageDataGenerator dan Augmentation
    - menggunakan metode split data (train dan validation)
    - train model (tanpa callback)
    - plot hasil training


- Model pada C2W3 lebih lengkap lagi:
    - jika sudah ada folder image nya dengan subdirectory label, maka bisa dibuat variabel path untuk masing-masing test dan validasi data set
    - lihat shape array dari image
    - buat fungsi training dan validasi dari folder, dan masukkan metode augmentation
    - dari fungsi di atas, buat variabel train dan validasi nya.
    - download transfer learning nya
    - buat variabel transfer learning
    - membuat fungsi untuk mengambil model transfer learning dan buat variabel pre_trained_model.
    - buat class Callback
    - membuat fungsi untuk mengambil last layer dari transfer learning
    - Buat fungsi modelnya
        - tekniknya dengan menambahkan layer secara manual.
        - masukkan metode regularization:dropout untuk mengatasi masalah overfitting
        - compile model
    - buat variabel model dari fungsi model di atas
    - train model dengan memasukkan parameter callback
    - plot hasil
    
