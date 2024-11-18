import threading
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def sort_with_algorithm(algorithm, arr, results, index):
    start_time = time.time()
    sorted_arr = algorithm(arr[:]) 
    end_time = time.time()
    results[index] = (sorted_arr, end_time - start_time)

unsorted_list = [34, 7, 23, 32, 5, 62, 14, 78, 50, 3, 10]
algorithms = [quicksort, mergesort, bubble_sort]
algorithm_names = ["Quicksort", "Mergesort", "Bubble Sort"]

threads = []
results = [None] * len(algorithms)

for i, algorithm in enumerate(algorithms):
    thread = threading.Thread(target=sort_with_algorithm, args=(algorithm, unsorted_list, results, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for i, (sorted_list, duration) in enumerate(results):
    print(f"{algorithm_names[i]}: Sorted list: {sorted_list}, Time taken: {duration:.6f} seconds")
