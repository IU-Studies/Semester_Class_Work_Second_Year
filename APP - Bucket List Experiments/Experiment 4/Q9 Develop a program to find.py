""" Develop a program to find the minimum number of attempts needed to find the critical floor in a
building with k floors using n eggs. """

def min_attempts(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = 0  
        dp[i][1] = 1  
    
    for j in range(1, k + 1):
        dp[1][j] = j  

    for i in range(2, n + 1):  
        for j in range(2, k + 1):  
            dp[i][j] = float('inf')  
            for x in range(1, j + 1):  
                worst_case = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                dp[i][j] = min(dp[i][j], worst_case)

    return dp[n][k]


n = 2  
k = 10  
result = min_attempts(n, k)
print("Minimum number of attempts needed with ", str(n), " eggs and ", str(k), " floors: ", str(result))
