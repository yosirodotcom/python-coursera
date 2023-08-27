import re

# Splitting the text into sentences using ".", "?", and "!" as delimiters
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

# Splitting the text into sentences while capturing the delimiters as well
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

# Replacing email addresses with "[REDACTED]"
print(
    re.sub(
        r"[\w.%+-]+@[\w.-]+",
        "[REDACTED]",
        "Received an email for go_nuts95@my.example.com",
    )
)

# Reversing the order of "Last Name, First Name" to "First Name Last Name"
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
