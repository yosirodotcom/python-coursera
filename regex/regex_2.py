import re

print(re.search(r"aza", "plaza"))
print(re.search(r"aza", "bazaar"))
print(re.search(r"aza", "maze")) # None

print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"a.e.i", "academia"))

print(re.search(r"p.ng", "Pangea", re.IGNORECASE))