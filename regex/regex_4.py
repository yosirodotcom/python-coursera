import re

print(re.search(r"Py.*n", "Pygmalionnt si"))
print(re.search(r"Py.*n", "Pygmalionnt sin"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"[aA].*[aA]", "banana")) # adanya pengulangan huruf A atau a
print(re.search(r"[aA].*[aA]", "Animal Kingdom")) 
print(re.search(r"[aA].*[aA]", "pineapple")) # none

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "wodly"))
print(re.search(r"o+l+", "wodoly"))
print(re.search(r"o+l+", "wooly"))

print(re.search(r"p?each", "To each their own")) # mencari kata peach atau each
print(re.search(r"p?each", "I like peaches"))





