user@ubuntu:~$ mkdir mynewdir # create folder/directory
user@ubuntu:~$ cd mynewdir # go to directory
user@ubuntu:~$ pwd # check current directory
user@ubuntu:~$ cd ../spider.txt # .. is previous directory
user@ubuntu:~$ touch myfile.txt # create empty file
user@ubuntu:~$ ls -l # tp see all files in this directory with complete information
user@ubuntu:~$ ls -la # to see hidden files
user@ubuntu:~$ mv myfile.txt mynewname.txt # rename file
user@ubuntu:~$ cp spider.txt spider_copy.txt # copy file
user@ubuntu:~$ rm * # remove all
user@ubuntu:~$ remdir mynewdir/ # remove empty directory

user@ubuntu:~$ ./stdout_example.py > new_file.txt # Write print result from python to text file (fungsin ini akan menimpa file yang lama)
user@ubuntu:~$ ./stdout_example.py >> new_file.txt # Append text
user@ubuntu:~$ echo "These are the contents of the file" > myecho.txt # dengan echo juga bisa menuliskan outputnya ke text
user@ubuntu:~$ ./streams_err.py < new_file.txt 2> error_file.txt # 2> is write error to the file that happen when entering command in bash


user@ubuntu:~$ ls -l | less # pipeline, berfungsi untuk melihat data yang sangat banyak, untuk keluar tekan Q.

user@ubuntu:~$ cat spider.txt | tr '''\n' | sort | uniq -c | sort -nr | head 
# cat spider.txt: Ini akan menampilkan isi file bernama "spider.txt". Perintah cat digunakan untuk menggabungkan dan menampilkan isi file di terminal.
# tr '\'''\n': Ini adalah perintah untuk mengganti setiap tanda kutip tunggal (') dengan karakter baris baru (\n). Ini mungkin sebuah kesalahan tipografi, karena karakter kutip tunggal tidak berpasangan.
# sort: Ini akan mengurutkan baris-baris yang dihasilkan dari langkah sebelumnya secara alfabetis.
# uniq -c: Ini akan menghitung jumlah kemunculan unik dari setiap baris dan menambahkannya di depan setiap baris.
# sort -nr: Ini akan mengurutkan baris-baris berdasarkan jumlah kemunculan secara numerik dalam urutan menurun (dari yang paling banyak ke yang paling sedikit).
# head: Ini akan mengambil 10 baris pertama dari keluaran yang dihasilkan dari langkah sebelumnya dan menampilkannya di terminal.

user@ubuntu:~$ cat capitalize.py
# #!/usr/bin/env python3
# import sys
# for line in sys.stdin:
#     print(line.strip().capitalize())
user@ubuntu:~$ cat haiku.txt
# advance your career.
# automating with Python.
# it's so fun to learn.
user@ubuntu:~$ cat haiku.txt | ./capitalize.py
# Advance your career.
# Automating with Python.
# it's so fun to learn.

# Penjelasan: 
# cat haiku.txt | ./capitalize.py: Ini adalah perintah yang mengalirkan isi berkas haiku.txt 
# ke skrip capitalize.py menggunakan aliran (pipe). Hasil keluaran dari perintah pertama akan menjadi masukan bagi perintah kedua.
# Hasil keluaran yang diperoleh adalah sama dengan masukan karena skrip capitalize.py hanya 
# mengubah setiap baris menjadi format kapitalisasi tanpa mengubah kontennya.

user@ubuntu:~$ ping www.google.com
# to interupt it, CTRL+C
# to pause/stop, CTRL+Z, to continue, fg

# we can also kill the process with other terminal
# assume there are 2 terminal, 1 ping, 1 for kill
user@ubuntu:~$ ps ax | grep ping
# akan diberikan PID yang bisa kita gunakan untuk mengakhiri proses ping
user@ubuntu:~$ kill 4619