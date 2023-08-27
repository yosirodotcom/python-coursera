#contional statement

#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi


if test -n "$PATH"; then echo "Your path is not empty"; fi
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

# Kedua baris kode tersebut memiliki arti yang sama dan menguji apakah variabel lingkungan $PATH tidak kosong.
# Baris ini menggunakan perintah test dengan opsi -n, yang menguji apakah string yang diberikan (dalam hal ini, isi dari variabel $PATH) tidak kosong. 