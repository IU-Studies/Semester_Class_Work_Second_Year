#Write a program that logs messages from multiple threads, ensuring that the log messages are thread-safe.

import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s',
    filename='thread_safe.log',
    filemode='a'
)

def log_messages(thread_id):
    for i in range(5):
        logging.info(f"Message {i} from thread {thread_id}")
        time.sleep(1)

threads = []
for thread_id in range(3): 
    thread = threading.Thread(target=log_messages, args=(thread_id,), name=f"Thread-{thread_id}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
