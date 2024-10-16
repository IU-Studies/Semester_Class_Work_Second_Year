""" Create a program that reads a text file and prints its contents to the console, demonstrating the use of
read(), readline(), and readlines() methods. """

file = open("example.txt", "r")

print("Using read():")
content = file.read()
print(content)
file.seek(0)

print("\nUsing readline():")
line = file.readline()
while line:
    print(line.strip())  
    line = file.readline()

file.seek(0)

print("\nUsing readlines():")
lines = file.readlines()
for line in lines:
    print(line.strip())

file.close()
