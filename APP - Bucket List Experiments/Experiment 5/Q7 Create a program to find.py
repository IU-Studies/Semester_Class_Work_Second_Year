""" Create a program to find the contiguous subarray within a one-dimensional array of numbers that
has the largest sum. """

def max_subarray_sum(arr):
    if len(arr) == 0:
        return 0

    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])

        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print("Maximum Subarray Sum:", result)
