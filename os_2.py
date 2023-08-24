# read file

file = open("spider.txt")
print(file.readline())  # print the first line
print(file.readline())  # print the second line

# atau menggunakan
print(file.read())  # untuk membaca semua isi dari text file
                    # dengan catatan tidak ada perintah file.readline() sebelumnya
file.close() # setelah file di buka harus selalu ditutup
   

# jika tidak ingin ada format close maka bisa menggunakan metode ini:

with open("spider.txt") as file:
    print(file.read())

# atau 
with open("hello_world.txt") as text:
    for line in text:
	    print(line.strip())

# atau
file = open("spider.txt")
lines = file.readlines()
file.close()

print(lines)
