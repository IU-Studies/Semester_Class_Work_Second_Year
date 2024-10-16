""" Develop a script that prompts the user for input and writes that data to a new text file, ensuring the file is
created or overwritten as needed. """

user_input = input("Enter the text you want to write to the file: ")

file = open("user_input.txt", "w")

file.write(user_input)

file.close()

print("Data has been written to user_input.txt")
