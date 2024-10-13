""" Implement a program to find the length of the longest increasing subsequence in an array of numbers """

def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

arr = [10, 9, 2, 5, 3, 7, 101, 18]  
result = longest_increasing_subsequence(arr)
print("Length of the longest increasing subsequence is: " + str(result))
