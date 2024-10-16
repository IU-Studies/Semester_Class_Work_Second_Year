""" Implement a program that reads a large text file line by line using a file iterator and counts the
occurrences of a specific word. """

file_path = input("Enter the file path: ")
word_to_search = input("Enter the word to count: ").lower()

word_count = 0

try:
    with open(file_path, "r") as file:
        for line in file:
            words = line.lower().split()
            word_count += words.count(word_to_search)

    print(f"The word '{word_to_search}' occurred {word_count} times.")
except FileNotFoundError:
    print("The file does not exist.")
