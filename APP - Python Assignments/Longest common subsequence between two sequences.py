#Longest common subsequence between two sequences.
from functools import lru_cache
def longest_common_subsequence(seq1, seq2):
    @lru_cache(None)
    def dp(i, j):
        if i == 0 or j == 0:
            return ""

        if seq1[i - 1] == seq2[j - 1]:
            return dp(i - 1, j - 1) + seq1[i - 1]

        else:
            lcs1 = dp(i - 1, j)
            lcs2 = dp(i, j - 1)
            return lcs1 if len(lcs1) > len(lcs2) else lcs2

    n, m = len(seq1), len(seq2)
    return dp(n, m)

seq1 = "CXMAABDRD"
seq2 = "ERKAABDCG"
result = longest_common_subsequence(seq1, seq2)
print(result)
