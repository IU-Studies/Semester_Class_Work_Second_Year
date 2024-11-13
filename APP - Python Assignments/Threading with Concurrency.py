import threading
import time
import random
import math

def download_data(file_id):
    print(f"Starting download for file {file_id}...\n")
    time.sleep(random.uniform(1,3))
    print(f"Download completed for file {file_id}.\n")
    time.sleep(1)

def calculate_factorial(number):
    print(f"Starting factorial calculation for {number}...\n")
    factorial = math.factorial(number)
    print(f"Factorial of {number} is {factorial}.\n")
    time.sleep(1)

threads = []
for file_id in range(1,4):
    thread = threading.Thread(target=download_data, args=(file_id,))
    threads.append(thread)

numbers = [5,7,10]
for number in numbers:
    thread = threading.Thread(target=calculate_factorial, args=(number,))
    threads.append(thread)

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("All tasks completed.")
