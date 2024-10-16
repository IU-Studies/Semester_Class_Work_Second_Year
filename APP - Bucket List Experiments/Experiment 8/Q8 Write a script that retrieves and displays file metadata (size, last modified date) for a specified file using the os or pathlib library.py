""" Write a script that retrieves and displays file metadata (size, last modified date) for a specified file using
the os or pathlib library. """

import os
import time

file_path = input("Enter the file path: ")

if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    
    last_modified_time = os.path.getmtime(file_path)
    readable_time = time.ctime(last_modified_time)
    
    print(f"File Size: {file_size} bytes")
    print(f"Last Modified: {readable_time}")
else:
    print("The file does not exist.")

#OR

from pathlib import Path

file_path = input("Enter the file path: ")

file = Path(file_path)

if file.exists():
    file_size = file.stat().st_size
  
    last_modified_time = file.stat().st_mtime
    readable_time = time.ctime(last_modified_time)
    
    print(f"File Size: {file_size} bytes")
    print(f"Last Modified: {readable_time}")
else:
    print("The file does not exist.")
