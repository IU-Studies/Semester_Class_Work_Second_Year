""" Write a program to determine the maximum value that can be obtained by putting items in a
knapsack with a given weight capacity. """

def knapsack(max_weight, weights, values, n):
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_weight]

weights = [2, 3, 4, 5]  
values = [3, 4, 5, 6]   
max_weight = 5          
n = len(weights)        

result = knapsack(max_weight, weights, values, n)
print("Maximum value that can be obtained:", result)
