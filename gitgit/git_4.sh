# Remote

user@ubuntu:~$ git remote -v # melihat link remote repositories
user@ubuntu:~$ git remote show origin # untuk mengambil perubahan dari remote repository ke local repository tanpa melakukan merge
user@ubuntu:~$ git branch -r # menampilkan daftar branch yang ada pada repository Git, termasuk branch yang berasal dari remote repository.
user@ubuntu:~$ git fetch # untuk melihat perubahan dari remote repository ke local repository tanpa melakukan merge.
user@ubuntu:~$ git pull # untuk mengambil perubahan dari remote repository ke local repository dan melakukan merge secara otomatis
user@ubuntu:~$ git remote update # untuk mengambil perubahan dari remote repository ke local repository tanpa melakukan merge

##------------------->
# Handling conflict 1
# ketika terjadi conflict pada saat push, maka
# gunakan git pull
# ketika terjadi conflict pada saat merge yang dilakukan git pull maka
# lihat di posisi mana yang conflict dengan git log --graph -- oneline -- all
# kemudian lihat bagian yang berkonflik dengan:
user@ubuntu:~$ git log -p origin/master # digunakan untuk menampilkan perubahan yang terjadi pada branch origin/master. Perintah ini akan menampilkan daftar commit yang ada pada branch origin/master, beserta perubahan yang terjadi pada setiap commit dalam format patch 
# setelah menemukan konflik tersebut, lakukan fix kode
# setelah selesai, git add dan git commit dan lakukan git push


##------------------->
# jika kita ingin membuat branch dari lokal dan push to remote sehingga berada di bawah master
user@ubuntu:~$ git checkout -b mybranch # buat dulu branch di lokal kemudian lakukan perubahan yang diinginkan, setelah selesai, lakukan di bawah ini
user@ubuntu:~$ git push -u origin mybranch # untuk mengirim perubahan pada branch mybranch ke remote repository origin. Perintah ini akan membuat branch refactor pada remote repository jika branch tersebut belum ada, dan mengatur branch refactor pada local repository untuk melakukan tracking terhadap branch origin/mybranch

##------------------->
# skenario rebase pertama (menyinkronkan commit dari master ke branch sebelum branch tersebut di merge ke master)
# lakukan pull ke master lokal
user@ubuntu:~$ git pull
# kemudian cek
user@ubuntu:~$ git log --graph --oneline --all
# terjadi beberapa tambahan commit pada master yang tak dimiliki oleh branch
# kemudian kita beralih ke branch
user@ubuntu:~$ git checkout mybranch
# dan lakukan rebas
user@ubuntu:~$ git rebase master
# kemudian cek
user@ubuntu:~$ git log --graph --oneline --all
# setelah di cek, kita bisa memastikan commit history pada branch sudah sejalan 
# dengan commit history pada master yang ada di remote
# sekarang kita menggabungkan kembali branch ke master
user@ubuntu:~$ git checkout master
user@ubuntu:~$ git merge mybranch
# jika sukses anda dapat menghapus branch tadi
# ketika sudah melakukan rebase, kembali master dan lakukan merge
# kemudian lakukan push
user@ubuntu:~$ git push --delete origin mybranch
user@ubuntu:~$ git branch -d mybranch
user@ubuntu:~$ git push


##------------------->
# Skenario rebase lainnya
# setelah melakukan commit di master branch, kita cek terlebih dahulu
# apakah ada perubahan pada master di remote oleh yang lainnya
user@ubuntu:~$ git fetch
# kemudian lakukan rebase
user@ubuntu:~$ git rebase origin/master
# jika terjadi conflict maka lihat opsi yang ditawarkan, jika ingin di fix code maka
# setelah diperbaiki
user@ubuntu:~$ git add namafileyangdiperbaiki
user@ubuntu:~$ git rebase --continue
# cek history
user@ubuntu:~$ git log --graph -oneline
# kemudian kita lakukan push
user@ubuntu:~$ git push

##------------------->
# Skenario rebase lainnya, squash commit

user@ubuntu:~$ git rebase -i master
# akan terbuka editor nano agar kita memilih commit mana yang akan di jadikan satu
# pilih line commit yang akan di squash dan ganti pick menjadi squash
# setelah di save dan keluar, maka akan tampil jendela nano lainnya
# Di sini kita bisa mengubah commit message, setelah selesai, keluar dari nano
# check commite dengan:
user@ubuntu:~$ git show
user@ubuntu:~$ git status
user@ubuntu:~$ git log --graph --oneline --all -4
# kemudian lakukan push
user@ubuntu:~$ git push
# jika terjadi warning, abaikan terlebih dahulu
user@ubuntu:~$ git push -f
