# for loops

#!/bin/bash

# Contoh 1
for fruit in peach orange apple; do
    echo "I like $fruit!"
done

# Contoh 2
for file in *.htm; do # Loop through all files ending in .htm

    name=$(basename "$file" .HTM) # Get filename without extension

    mv "$file" "$name.html" # Rename file to .html

done

# tapi sebelum kita melakukan fungsi di atas bisa kita intip dulu hasilnya dengan cara
for file in *.htm; do 
    name=$(basename "$file" .HTM)
    echo mv "$file" "$name.html" 
done