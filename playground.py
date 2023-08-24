def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)

    with open(filename, "r") as f:
        filesize = len(f.readline())
    return filesize


print(create_python_script("program.py"))
