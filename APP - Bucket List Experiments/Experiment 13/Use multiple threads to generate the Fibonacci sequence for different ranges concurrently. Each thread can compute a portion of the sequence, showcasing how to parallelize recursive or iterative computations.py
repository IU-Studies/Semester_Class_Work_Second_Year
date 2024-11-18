import threading

def fibonacci_range(start, end, results, index):
    fib_sequence = []
    a, b = 0, 1
    for i in range(end + 1):
        if i >= start:
            fib_sequence.append(a)
        a, b = b, a + b
    results[index] = fib_sequence

def parallel_fibonacci(ranges):
    threads = []
    results = [None] * len(ranges)

    for index, (start, end) in enumerate(ranges):
        thread = threading.Thread(target=fibonacci_range, args=(start, end, results, index))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    merged_sequence = []
    for part in results:
        merged_sequence.extend(part)
    return merged_sequence

# Example usage
ranges = [(0, 10), (11, 20), (21, 30)]  # Define the ranges for Fibonacci computation
fib_sequence = parallel_fibonacci(ranges)
print("Fibonacci sequence:", fib_sequence)
