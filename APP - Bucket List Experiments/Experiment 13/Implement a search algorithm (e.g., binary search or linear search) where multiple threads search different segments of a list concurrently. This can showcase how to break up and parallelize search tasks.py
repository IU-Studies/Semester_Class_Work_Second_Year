import threading

def search_segment(segment, target, result, index):
    for i, value in enumerate(segment):
        if value == target:
            result[index] = i
            return
    result[index] = -1  

def parallel_search(numbers, target, num_threads):
    segment_size = len(numbers) // num_threads
    threads = []
    results = [None] * num_threads

    for i in range(num_threads):
        start = i * segment_size
        end = (i + 1) * segment_size if i < num_threads - 1 else len(numbers)
        segment = numbers[start:end]
        thread = threading.Thread(target=search_segment, args=(segment, target, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for i, relative_index in enumerate(results):
        if relative_index != -1:
            return i * segment_size + relative_index  

    return -1 

numbers = [10, 23, 45, 6, 78, 34, 89, 12, 67, 90, 56]
target = 34
num_threads = 3
result = parallel_search(numbers, target, num_threads)
print("Target found at index:", result if result != -1 else "Not found")
