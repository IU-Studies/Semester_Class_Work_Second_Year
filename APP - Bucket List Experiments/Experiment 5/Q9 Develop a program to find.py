""" Develop a program to find the most efficient way to multiply a chain of matrices. """

import sys

def matrix_chain_order(p):
    n = len(p) - 1  
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = sys.maxsize

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]

p = [1, 2, 3, 4]
result = matrix_chain_order(p)
print("Minimum number of multiplications:", result)
