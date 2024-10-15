""" Implement a program to find the length of the shortest common supersequence of two strings. """

def shortest_common_supersequence(X, Y):
    m = len(X)
    n = len(Y)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    
    scs_length = m + n - lcs_length

    return scs_length

X = "AGGTAB"
Y = "GXTXAYB"

result = shortest_common_supersequence(X, Y)
print("Length of the shortest common supersequence:", result)
