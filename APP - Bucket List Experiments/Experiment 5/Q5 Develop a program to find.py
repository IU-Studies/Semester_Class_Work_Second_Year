""" Develop a program to find the longest subsequence in an array of integers that is strictly increasing. """

def longest_increasing_subsequence(arr):
    n = len(arr)

    if n == 0:
        return []

    dp = [1] * n  
    prev = [-1] * n  

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    lis_index = dp.index(max_len)

    lis = []
    while lis_index != -1:
        lis.append(arr[lis_index])
        lis_index = prev[lis_index]

    lis.reverse()

    return lis

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest_increasing_subsequence(arr)
print("Longest Increasing Subsequence:", result)
