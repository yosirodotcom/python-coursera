user@ubuntu:~$ git init # membuat file git di directory yang akan kita git
user@ubuntu:~$ ls -la # untuk melihat file git 
user@ubuntu:~$ ls - l .git/ # untuk melihat isi dari file git
user@ubuntu:~$ git config --global user.name "Name"
user@ubuntu:~$ git config --global user.email "user@example.com"


user@ubuntu:~$ git add "nama file" # menambahkan file ke vcs
user@ubuntu:~$ git add -p # digunakan untuk melakukan "patch mode" pada perintah git add. Ini memungkinkan Anda untuk memilih secara interaktif bagian-bagian (hunks) dari perubahan pada berkas yang akan di-"stage" (diindeks) untuk komit selanjutnya.
y: Yes, untuk menambahkan hunk ke dalam staging area.
n: No, untuk tidak menambahkan hunk ke dalam staging area.
s: Split, untuk memecah hunk menjadi bagian-bagian yang lebih kecil.
e: Edit, untuk mengedit hunk sebelum menambahkannya.

user@ubuntu:~$ git status # melihat status
user@ubuntu:~$ git diff # perintah yang digunakan dalam Git untuk melihat perbedaan antara dua titik dalam sejarah repositori. Perintah ini membandingkan perubahan pada berkas-berkas antara dua komit, biasanya komit yang sedang diindeks (staging area) dengan komit terakhir atau komit sebelumnya.
user@ubuntu:~$ git diff --staged # digunakan untuk melihat perbedaan antara berkas-berkas yang ada di staging area (indeks) dengan komit terakhir yang Anda telah buat. Dengan kata lain, perintah ini memungkinkan Anda melihat perubahan yang telah di-"stage" (diindeks) untuk komit, tetapi belum di-commit.
user@ubuntu:~$ git diff "nama file" # melihat perubahan
user@ubuntu:~$ git commit -m 'messenge that we want to write'
user@ubuntu:~$ git commit -a -m 'messege here' # untuk melakukan commit tanpa harus commit add terlebih dahulu
user@ubuntu:~$ git config -l # to see setting
user@ubuntu:~$ git log # to track git 
user@ubuntu:~$ git log -p # git log yang terasosiasi dengan patch
user@ubuntu:~$ git log --stat
user@ubuntu:~$ git log -1 # melihat commit 1 langkah belakang
user@ubuntu:~$ git log -2 # melihat commit 2 langkah ke belakang
user@ubuntu:~$ git show idcommit # change idcommit to show only commit with id reference

user@ubuntu:~$ git rm namefile # remove file diikuti dengan commit
user@ubuntu:~$ git mv oldname newname # rename file atau move file diikuti dengan commit
user@ubuntu:~$ echo nametoignore > .gitignore # ignore file to git in repo

# Revert changes
user@ubuntu:~$ git checkout namafile # to restore file before it's staged.
user@ubuntu:~$ git reset HEAD namafile # to unstage (before commit), revert to git add
user@ubuntu:~$ git commit --amend # memasukkan file yang dirubah ke dalam commit terakhir, 
# jadi tidak perlu membuat commit tambahan. 
# tapi sebelumnya lakukan git add terlebih dahulu.
# ini juga bisa disebut fix commit terakhir
user@ubuntu:-$ git revert HEAD # to revert the last commit
user@ubuntu:-$ git revert commitid # to revert specific commit

