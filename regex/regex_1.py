## pada bash shell

# untuk mencari kata-kata yang mengandung 'thon' case sensitive
# ~$ grep thon /usr/...

# untuk mencari kata-kata tanpa harus case sensitive
# ~$ grep -i thon /usr/...

# untuk mencari kata-kat yang mengandung huruf dari l dengan akhiran rts
# ~$ grep l.rts /usr/...
# nanti hasilnya bisa alerts, blurts, flirts

# mencari kata yang berawalan character tertentu
# ~$ grep ^fruit /usr/...
# hasilnya bisa fruitier, fruitiest

# mencari kata yang berakhiran character tertentu
# ~$ grep cat$ /usr/...
# hasilnya bisa muscat, bobcat