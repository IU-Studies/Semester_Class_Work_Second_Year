#Implement a Python program that creates multiple threads to perform different tasks concurrently.
import time
import random
import math
import threading

def download_data(file_id):
    print(f"Starting download for file {file_id}...\n")
    time.sleep(random.uniform(1, 3))
    print(f"Download completed for file {file_id}.\n")
    time.sleep(1)

def calculate_factorial(number):
    print(f"Starting factorial calculation for {number}...\n")
    factorial = math.factorial(number)
    print(f"Factorial of {number} is {factorial}.\n")
    time.sleep(1)

# Create threads for downloading files
file_threads = []
for file_id in range(1, 4):
    thread = threading.Thread(target=download_data, args=(file_id,))
    file_threads.append(thread)
    thread.start()

# Create threads for calculating factorials
factorial_threads = []
numbers = [5, 7, 10]
for number in numbers:
    thread = threading.Thread(target=calculate_factorial, args=(number,))
    factorial_threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in file_threads + factorial_threads:
    thread.join()

print("All tasks completed.")
