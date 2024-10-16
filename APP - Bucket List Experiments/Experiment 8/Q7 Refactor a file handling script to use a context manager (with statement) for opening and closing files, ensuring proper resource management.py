""" Refactor a file handling script to use a context manager (with statement) for opening and closing files,
ensuring proper resource management. """

with open("example.txt", "r") as file:
    content = file.read()

print(content)
