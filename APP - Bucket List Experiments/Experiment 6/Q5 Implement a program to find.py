""" Implement a program to find whether a subset of a given set of integers sums up to a given target. """

def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][target]

nums = [3, 34, 4, 12, 5, 2]
target = 9

result = subset_sum(nums, target)
print("Is there a subset with the target sum?:", result)
