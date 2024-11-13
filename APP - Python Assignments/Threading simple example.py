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

for file_id in range(1,4):
    download_data(file_id)

numbers = [5,7,10]

for number in numbers:
    calculate_factorial(number)

print("All tasks completed.")
