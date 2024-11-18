import threading

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            print(f"Word count for {file_path}: {word_count}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

threads = []
file_paths = ["file1.txt", "file2.txt", "file3.txt"]  # Replace with your file paths

for path in file_paths:
    thread = threading.Thread(target=count_words, args=(path,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()