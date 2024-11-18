#Use threads to find prime numbers in different ranges concurrently. 
#Each thread works on a separate range and prints the primes found within its range.

import threading

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    print(f"Primes in range {start}-{end}: {primes}")

ranges = [(10, 50), (51, 100), (101, 150)] 
threads = []

for start, end in ranges:
    thread = threading.Thread(target=find_primes_in_range, args=(start, end))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
