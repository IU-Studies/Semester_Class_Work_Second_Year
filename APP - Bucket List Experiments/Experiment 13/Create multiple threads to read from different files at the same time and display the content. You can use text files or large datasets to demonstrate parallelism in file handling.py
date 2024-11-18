import threading

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File {file_path} not found.")

threads = []
file_paths = ["file1.txt", "file2.txt", "file3.txt"]  # Replace with your file paths

for path in file_paths:
    thread = threading.Thread(target=read_file, args=(path,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()