""" Implement a program that reads a large CSV file line by line, counts the total number of entries, and
outputs the count without loading the entire file into memory. """

import csv

def count_csv_entries(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            row_count = sum(1 for row in reader) - 1  
        print(f"Total number of entries (excluding header): {row_count}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

csv_file_path = 'large_file.csv'  

count_csv_entries(csv_file_path)
