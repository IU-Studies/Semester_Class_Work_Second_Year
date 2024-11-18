import threading

def sort_sublist(sublist, results, index):
    results[index] = sorted(sublist)

def merge_sorted_lists(sorted_lists):
    result = []
    indices = [0] * len(sorted_lists)

    while True:
        min_val = None
        min_idx = -1

        for i, lst in enumerate(sorted_lists):
            if indices[i] < len(lst):
                if min_val is None or lst[indices[i]] < min_val:
                    min_val = lst[indices[i]]
                    min_idx = i

        if min_val is None:
            break

        result.append(min_val)
        indices[min_idx] += 1

    return result

def concurrent_sort(numbers, num_threads):
    chunk_size = len(numbers) // num_threads
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    results = [None] * len(chunks)

    threads = []
    for index, chunk in enumerate(chunks):
        thread = threading.Thread(target=sort_sublist, args=(chunk, results, index))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return merge_sorted_lists(results)

numbers = [34, 7, 23, 32, 5, 62, 14, 78, 50, 3, 10]
num_threads = 3  # Number of threads
sorted_numbers = concurrent_sort(numbers, num_threads)
print("Sorted list:", sorted_numbers)
