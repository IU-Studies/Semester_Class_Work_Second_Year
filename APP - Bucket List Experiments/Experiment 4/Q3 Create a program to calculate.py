""" Create a program to calculate the number of unique paths from the top-left corner to the
bottom-right corner of a grid, moving only right or down """

def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        dp[i][0] = 1  
    for j in range(n):
        dp[0][j] = 1  

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]

m = 3  
n = 7  
result = unique_paths(m, n)
print("Number of unique paths in a ",str(m), "x", str(n), " grid: ", str(result))
