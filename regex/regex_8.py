import re

log1 = (
    "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
)
log2 = "A completely different string that also has numbers [34567]"
log3 = "99 elephants in a [cage]"

# Regular expression pattern to capture the process id inside square brackets
regex = r"\[(\d+)\]"

# Searching for a match using the regular expression in log1
result = re.search(regex, log1)
print(result[1])  # Printing the content of the first capturing group (process id)

# Searching for a match using the regular expression in log2
result = re.search(regex, log2)
print(result[1])  # Printing the content of the first capturing group (process id)

# Untuk log 3 maka akan terjadi error, untuk itu
# kita bisa menggunakan metode berikut


def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]


print(extract_pid(log3))
