import re


"""
Py: This part of the pattern matches the characters "Py" literally.
.*: This is a combination of characters that work together:
    .: This dot is a wildcard that matches any single character (except a newline).
    *: This asterisk is a quantifier that means "zero or more occurrences." So, .* matches zero or more of any character.
n: This part of the pattern matches the character "n" literally.
"""
print(re.search(r"Py.*n", "Pygmalionnt si"))
print(re.search(r"Py.*n", "Pygmalionnt sin"))
print(re.search(r"Py.*n", "Python Programming"))


"""
Py: This part of the pattern matches the characters "Py" literally.
[a-z]*: This character class [a-z] matches any lowercase letter, and * is a quantifier that means "zero or more occurrences." So, [a-z]* matches zero or more lowercase letters.
n: This part of the pattern matches the character "n" literally.
"""
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

"""
[aA]: This character class [aA] matches either "a" or "A", allowing for either uppercase or lowercase "a".
.*: This is a wildcard combination that matches any number of characters (except newline). The * quantifier means "zero or more occurrences."
[aA]: Another occurrence of the character class [aA], matching "a" or "A".
"""
print(re.search(r"[aA].*[aA]", "banana"))  # adanya pengulangan huruf A atau a
print(re.search(r"[aA].*[aA]", "An9imal Kingdom"))
print(re.search(r"[aA].*[aA]", "pineapple"))  # none

"""
"." sifatnya hanya untuk huruf
"*" sifatnya hanya untuk angka
".*" sifatnya untuk huruf dan angka
"""

"""
o: This character matches the letter "o" literally.
+: This is a quantifier that means "one or more occurrences." It applies to the character immediately preceding it.
l: This character matches the letter "l" literally.
+: This is another quantifier that means "one or more occurrences." It applies to the character immediately preceding it.
"""
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "wodly"))
print(re.search(r"o+l+", "wodoly"))
print(re.search(r"o+l+", "wooly"))


"""
p: This character matches the letter "p" literally.
?: This is a quantifier that means "zero or one occurrence." It applies to the character immediately preceding it. In this case, it allows for the possibility of the letter "p" to appear or not appear.
each: This part of the pattern matches the word "each" literally.
"""
print(re.search(r"p?each", "To each their own"))  # mencari kata peach atau each
print(re.search(r"p?each", "I like peaches"))
