# character apa saja akan ditemukan jika menggunakan []
import re

"""
[Pp]: This character class matches either "P" or "p". The brackets [...] indicate a character class, and inside it, Pp means either "P" or "p".
ython: This part of the pattern matches the literal characters "ython".
"""
print(re.search(r"[Pp]ython", "Python"))

"""
[a-z]: This character class matches any lowercase letter.
way: This literal part of the pattern matches the characters "way" literally.
"""
print(
    re.search(r"[a-z]way", "The end of the highway")
)  # a-z artinya huruf kecil a sampai z
print(
    re.search(r"[a-z]way", "what a way to go")
)  # None karena tidak ada satu pun huruf yang membersamai kata way

"""
cloud: This part of the pattern matches the word "cloud" literally.
[a-zA-Z0-9]: This character class matches a single character that is either an uppercase letter (A-Z), a lowercase letter (a-z), or a digit (0-9).
"""
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))


"""
This character class uses the caret ^ as the negation operator within the square brackets. It matches a single character 
that is not within the range of uppercase letters (A-Z) or lowercase letters (a-z)
"""
print(
    re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")
)  # mencari character yang bukan huruf (dalam  hal ini spasi merupakan character pertama yang ditemui yang bukan huruf)


"""
This character class uses the caret ^ as the negation operator within the square brackets. It matches a single character 
that is not within the range of uppercase letters (A-Z), lowercase letters (a-z), or a space.
"""
print(
    re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")
)  # mencari character yang bukan huruf dan spasi (dalam hal ini cuma simbol titik yang bukan huruf atau spasi)

"""
cat: This part of the pattern matches the word "cat" literally.

|: This is the alternation operator, which functions as an "OR" operator in regular expressions. It allows you to match either the expression on the left side or the expression on the right side.

dog: This part of the pattern matches the word "dog" literally.
"""
print(re.search(r"cat|dog", "I like cats."))
print(
    re.search(r"cat|dog", "I like both dogs and cats")
)  # hanya dog yang match, sehingga kita gunakan:
print(re.findall(r"cat|dog", "I like both dogs and cats"))
