""" Implement a program to calculate the minimum number of operations (insertions, deletions,
substitutions) required to convert one string into another """

def levenshtein_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i  
    for j in range(n + 1):
        dp[0][j] = j  

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])  
                dp[i][j] += 1

    return dp[m][n]

str1 = "kitten"
str2 = "sitting"

result = levenshtein_distance(str1, str2)
print("Minimum number of operations required:", result)
