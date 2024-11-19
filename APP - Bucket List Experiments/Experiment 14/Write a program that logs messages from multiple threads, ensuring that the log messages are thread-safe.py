import logging
import threading
import time

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s',
    filename='thread_safe.log',
    filemode='a'
)

# Function for threads to log messages
def log_messages(thread_id):
    for i in range(5):
        logging.info(f"Message {i} from thread {thread_id}")
        time.sleep(1)

# Create multiple threads
threads = []
for thread_id in range(3):  # Create 3 threads for demonstration
    thread = threading.Thread(target=log_messages, args=(thread_id,), name=f"Thread-{thread_id}")
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
