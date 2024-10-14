""" Design a program to determine whether a subset of a given set of numbers adds up to a specific target sum. """

def is_subset_sum(numbers, target_sum):
    n = len(numbers)
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True  

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if numbers[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - numbers[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target_sum]

numbers = [3, 34, 4, 12, 5, 2]  
target_sum = 9                   
result = is_subset_sum(numbers, target_sum)

if result:
    print("There is a subset with the target sum.")
else:
    print("There is no subset with the target sum.")
