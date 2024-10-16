""" Write a Python script that opens a file in different modes (read, write, append) and demonstrates the
correct method to close each file after use. """

file_read = open("example.txt", "r")
content = file_read.read()
print("Reading file content:\n", content)
file_read.close()

file_write = open("example.txt", "w")
file_write.write("This is new content written to the file.\n")
file_write.close()

file_append = open("example.txt", "a")
file_append.write("This is additional content appended to the file.\n")
file_append.close()
