import re

"""
This is the regular expression pattern you're searching for. 
It's a simple pattern that looks for the sequence of characters "aza".
"""
print(re.search(r"aza", "plaza"))
print(re.search(r"aza", "bazaar"))
print(re.search(r"aza", "maze"))  # None

print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
'''
r"a.e.i": This is the regular expression pattern you're searching for. It consists of:
a: The letter "a".
.: This dot is a wildcard that matches any single character except a newline.
e: The letter "e".
.: Another wildcard.
i: The letter "i".
'''
print(re.search(r"a.e.i", "academia"))

print(re.search(r"p.ng", "Pangea", re.IGNORECASE))
