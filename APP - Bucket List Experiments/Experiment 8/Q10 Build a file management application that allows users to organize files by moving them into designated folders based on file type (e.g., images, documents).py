""" Build a file management application that allows users to organize files by moving them into designated
folders based on file type (e.g., images, documents). """

import os
import shutil

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

source_dir = input("Enter the source directory path: ")

def organize_files(source_directory):
    if not os.path.exists(source_directory):
        print("The source directory does not exist.")
        return

    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            
            moved = False
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(source_directory, category)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    
                    shutil.move(file_path, destination_folder)
                    moved = True
                    print(f"Moved: {filename} -> {destination_folder}")
                    break

            if not moved:
                others_folder = os.path.join(source_directory, "Others")
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, others_folder)
                print(f"Moved: {filename} -> {others_folder}")

organize_files(source_dir)
