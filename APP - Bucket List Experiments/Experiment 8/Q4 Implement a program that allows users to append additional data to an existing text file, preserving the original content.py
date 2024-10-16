""" Implement a program that allows users to append additional data to an existing text file, preserving the
original content. """

user_input = input("Enter the text you want to append to the file: ")

file = open("existing_file.txt", "a")

file.write(user_input + "\n") 

file.close()

print("Data has been appended to existing_file.txt")
