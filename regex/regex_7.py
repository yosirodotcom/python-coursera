import re

# Searching for a pattern where the input starts with last name, followed by a comma and a space, and then the first name
# The regular expression has two capturing groups (\w*) to capture the last name and first name separately
"""
^: This anchor asserts the start of the string.

(\w*): This is a capturing group that matches zero or more word characters (letters, digits, underscores). It captures the first word.

, : This matches a comma and a space literally.

(\w*): Another capturing group that matches zero or more word characters. It captures the second word.

$: This anchor asserts the end of the string.
"""
print(re.search(r"^(\w*), (\w*)$", "lastname, firstname"))
print(re.search(r"^(\w*), (\w*)$", "last name, firstname"))  # None

result = re.search(r"^(\w*), (\w*)$", "lastname, firstname")
print(result.group())
print(result[0])
print(result[1])
print(result[2])

"""
^: This anchor asserts the start of the string.

([\w .-]*): This is a capturing group that matches zero or more occurrences of word characters, spaces, dots, dashes, and underscores. It captures the first phrase.

, : This matches a comma and a space literally.

([\w .-]*): Another capturing group that matches zero or more occurrences of the allowed characters. It captures the second phrase.

$: This anchor asserts the end of the string
"""


def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)


"""
[a-zA-Z]: This character class matches any single alphabetical character, whether uppercase (A-Z) or lowercase (a-z).

{5}: This is a quantifier that specifies exactly 5 occurrences of the preceding element. In this case, it applies to the character class [a-zA-Z]
"""
# Searching for a sequence of 5 consecutive alphabetical characters
print(re.search(r"[a-zA-Z]{5}", "a ghost"))

# Searching for a sequence of 5 consecutive alphabetical characters
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# Finding all sequences of 5 consecutive alphabetical characters
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))


"""
\b: This is a word boundary anchor that matches the position between a word character and a non-word character. It ensures that the pattern matches complete words.

[a-zA-Z]: This character class matches any single alphabetical character, whether uppercase (A-Z) or lowercase (a-z).

{5}: This is a quantifier that specifies exactly 5 occurrences of the preceding element. In this case, it applies to the character class [a-zA-Z].

\b: Another word boundary anchor to ensure the pattern matches complete words.
"""
# Finding all whole words with 5 consecutive alphabetical characters
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))


"""
\w: This is a metacharacter that matches any word character (letters, digits, underscores).

{5,10}: This is a quantifier that specifies a range of occurrences. In this case, it means that 
the preceding element (in this case, \w) should appear between 5 and 10 times.
"""
# Finding all sequences of word characters with a length between 5 and 10
print(re.findall(r"\w{5,10}", "I really like strawberries"))

"""
\w: This is a metacharacter that matches any word character (letters, digits, underscores).

{5,}: This is a quantifier that specifies a minimum number of occurrences. In this case, it means that 
the preceding element (in this case, \w) should appear at least 5 times.
"""
# Finding all sequences of word characters with a minimum length of 5
print(re.findall(r"\w{5,}", "I really like strawberries"))

'''
s: This matches the letter "s" literally.

\w{,20}: This matches zero to 20 word characters (letters, digits, underscores).

\w: This is a metacharacter that matches any word character (letters, digits, underscores).

{,20}: This is a quantifier that specifies a maximum number of occurrences. In this case, it 
means that the preceding element (in this case, \w) can appear up to 20 times.
'''
# Finding all sequences of word characters starting with 's' and up to 20 characters
print(re.findall(r"s\w{,20}", "I really like strawberries"))

# Finding all whole words with at least 7 characters
print(
    re.findall(r"\b\w{7,}\b", "I also have a taste for hot chocolate in the afternoon.")
)
