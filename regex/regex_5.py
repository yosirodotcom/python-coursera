import re

# Jika kita menggunakan tanda (.) maka itu artinya 1 char apapun itu
print(re.search(r".com", "welcome"))

# tapi bagaimana jika yang kita maksud memang ".com" 
# maka kita bisa menggunakan character escape (\)

print(re.search(r"\.com", "mydomain.com"))

# mencari sebuah kata, jika dalam kalimat maka kata pertama yang didapat
print(re.search(r"\w*", "mydomain.com"))
print(re.search(r"\w*", "mydomain_com"))
print(re.search(r"\w*", "mydomain com"))

# mencari 2 kata yang terpisah dengan spasi
print(re.search(r"\w+\s+\w+", "One"))
print(re.search(r"\w+\s+\w+", "123    Ready Set GO"))
print(re.search(r"\w+\s+\w+", "username user_01"))
print(re.search(r"\w+\s+\w+", "shopping_list: milk, bread, eggs."))