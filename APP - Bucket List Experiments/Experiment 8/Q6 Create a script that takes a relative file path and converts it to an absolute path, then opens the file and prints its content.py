""" Create a script that takes a relative file path and converts it to an absolute path, then opens the file and
prints its content. """

import os

relative_path = input("Enter the relative file path: ")

absolute_path = os.path.abspath(relative_path)
print("Absolute path:", absolute_path)

try:
    with open(absolute_path, "r") as file:
        content = file.read()
        print("\nFile content:")
        print(content)
except FileNotFoundError:
    print("The file does not exist at the specified path.")
