import os
# get working directory
print(os.getcwd())

# create folder
os.mkdir("new_dir")

# change working directory
os.chdir("new_dir")

# remove folder kosong
os.rmdir("new_dir")

# melihat isi semua file yang ada di folder
os.listdir("namafolder")

# mendeteksi apakah isi sebuah folder itu berisi file atau folder lagi
for name in os.listdir("namafolder"):
    fullname = os.path.join("namafolder", name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print("{fullname} is a file")

