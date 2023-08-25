# character apa saja akan ditemukan jika menggunakan []
import re

print(re.search(r"[Pp]ython", "Python"))
print(
    re.search(r"[a-z]way", "The end of the highway")
)  # a-z artinya huruf kecil a sampai z
print(
    re.search(r"[a-z]way", "what a way to go")
)  # None karena tidak ada satu pun huruf yang membersamai kata way

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

print(
    re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")
)  # mencari character yang bukan huruf (dalam  hal ini spasi merupakan character pertama yang ditemui yang bukan huruf)
print(
    re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")
)  # mencari character yang bukan huruf dan spasi (dalam hal ini cuma simbol titik yang bukan huruf atau spasi)

print(re.search(r"cat|dog", "I like cats."))
print(
    re.search(r"cat|dog", "I like both dogs and cats")
)  # hanya dog yang match, sehingga kita gunakan:
print(re.findall(r"cat|dog", "I like both dogs and cats"))
