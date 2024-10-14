""" Write a program to find the shortest sequence that has both input sequences as subsequences """

def lcs(str1, str2):
    m, n = len(str1), len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_str.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_str))

def shortest_common_supersequence(str1, str2):
    lcs_str = lcs(str1, str2)

    i, j = 0, 0

    scs = []

    for c in lcs_str:
        while str1[i] != c:
            scs.append(str1[i])
            i += 1
        while str2[j] != c:
            scs.append(str2[j])
            j += 1
        scs.append(c)
        i += 1
        j += 1

    scs.append(str1[i:])
    scs.append(str2[j:])

    return ''.join(scs)

str1 = "abac"
str2 = "cab"

result = shortest_common_supersequence(str1, str2)
print("Shortest Common Supersequence:", result)
