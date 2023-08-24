# Soal 1


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)

    with open(filename, "r") as f:
        filesize = len(f.readline())
    return filesize


print(create_python_script("program.py"))


# Soal 4
import os
import datetime


def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        pass
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    formattime = str(datetime.datetime.fromtimestamp(timestamp))
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return "{:.10s}".format(formattime)


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
