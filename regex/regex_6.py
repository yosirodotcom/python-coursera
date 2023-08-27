import re

"""
^: This anchor asserts the start of the string.

[A-Z]: This character class matches an uppercase letter at the beginning of the sentence.

[a-z]*: This matches zero or more lowercase letters that follow the initial uppercase letter.

(\s[a-z]*)*: This group captures zero or more sequences that consist of a space followed by lowercase letters. This allows for the possibility of multiple words separated by spaces.

[\.!?]: This character class matches one of the specified punctuation marks at the end of the sentence: ".", "?", or "!".

$: This anchor asserts the end of the string.
"""
# cek apakah ini merupakan sebuah kalimat lengkap.
print(re.search(r"^[A-Z][a-z]*(\s[a-z]*)*[\.!?]$", "Is this is a sentence?"))
print(re.search(r"^[A-Z][a-z]*(\s[a-z]*)*[\.!?]$", "1-2-3-GO!"))

# ingin dicari potongan kata yang dimulai dari A hingga a
print(re.search(r"A.*a", "Azerbaijan"))

# ingin dicari kata yang berawalan A dan berakhiran n
print(re.search(r"^A.*n$", "Azerbaijan"))

# ingin dicek apakah penulisan variabel sudah sesuai kaidah
print(re.search(r"^[a-zA-Z_][a-zA-z0-9_]*$", "_this_is_valid_variable_name"))
print(
    re.search(r"^[a-zA-Z_][a-zA-z0-9_]*$", "1this_is_valid_variable_name")
)  # not valid
