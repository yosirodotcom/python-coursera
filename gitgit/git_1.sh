user@ubuntu:~$ diff code1.py code2.py # mencari perbedaan 2 penulisan code
user@ubuntu:~$ diff -u code1.py code2.py # membuat tampilan lebih lengkap
user@ubuntu:~$ dif -u old_file new_file > change.diff # untuk menyimpan hasil diff
user@ubuntu:~$ patch file_will_merge < change.diff