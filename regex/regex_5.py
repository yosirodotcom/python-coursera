import re

# Jika kita menggunakan tanda (.) maka itu artinya 1 char apapun itu
print(re.search(r".com", "welcome"))

# tapi bagaimana jika yang kita maksud memang ".com"
# maka kita bisa menggunakan character escape (\)

print(re.search(r"\.com", "mydomain.com"))

# mencari sebuah kata, yang jika kata tersebut di klik 2 kali bisa terselect semua
"""
\w: This is a metacharacter that matches any word character. Word characters include letters (both uppercase and lowercase), digits, and underscores.
*: This is a quantifier that means "zero or more occurrences." It applies to the character immediately preceding it.
"""
print(re.search(r"\w*", "mydomain.com"))
print(re.search(r"\w*", "mydomain_com"))
print(re.search(r"\w*", "mydomain com"))

"""
\w+: This is a metacharacter that matches one or more word characters (letters, digits, underscores).
\s+: This is a metacharacter that matches one or more whitespace characters, including spaces, tabs, and newlines.
\w+: Another occurrence of the metacharacter that matches one or more word characters.
"""
# mencari 2 kata yang terpisah dengan spasi
print(re.search(r"\w+\s+\w+", "One"))
print(re.search(r"\w+\s+\w+", "123    Ready Set GO"))
print(re.search(r"\w+\s+\w+", "username user_01"))
print(re.search(r"\w+\s+\w+", "shopping_list: milk, bread, eggs."))

"""
the + symbol is a quantifier that indicates "one or more occurrences" of the preceding element. 
The preceding element can be a character, a group of characters, or a metacharacter.

For example, (abc)+ will match "abc", "abcabc", "abcabcabc", and so on.
\d+ will match "x123", "$456", "%789", and so on
"""
