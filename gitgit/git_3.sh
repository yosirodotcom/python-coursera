# Branch

user@ubuntu:~$ git branch # to see all branch
user@ubuntu:~$ git branch namebranch # create a new branch
user@ubuntu:~$ git checkout namebranch # to switch the new branch
user@ubuntu:~$ git checkout -b namebranch # create a new branch and switch to it
user@ubuntu:~$ git brach -d namebranch # delete branch, do it in master branch
user@ubuntu:~$ git merge namebranch # merge to master branch, do it in master branch. ini merupakn tipe fast forward merge

# manage conflict
user@ubuntu:~$ git status # untuk melihat apa2 saja yang terjadi di git saat ini
# ketika terjadi conflict pada merge, maka file yang berkonflik di master
# akan ditambahkan code bagian mana yang berkonflik untuk kita selesaikan
# secara manual. Setelah itu lakukan add dan commit


user@ubuntu:~$ git log --graph --oneline # untuk melihat commit dan branch secara grafik
user@ubuntu:~$ git merge --abort # untuk membatalkan perintah merge