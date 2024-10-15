""" Write a program to determine whether a given set can be partitioned into two subsets with equal sums. """

def can_partition(nums):
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

nums = [1, 5, 11, 5]

result = can_partition(nums)
print("Can the set be partitioned into two subsets with equal sums?:", result)
