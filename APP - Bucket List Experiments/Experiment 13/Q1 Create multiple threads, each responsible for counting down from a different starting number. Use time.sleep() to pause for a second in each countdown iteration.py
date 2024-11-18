import threading
import time

def countdown(start):
    while start > 0:
        print(start)
        start -= 1
        time.sleep(1)

threads = []
start_numbers = [10, 7, 5]  # Example starting numbers for countdowns

for number in start_numbers:
    thread = threading.Thread(target=countdown, args=(number,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
