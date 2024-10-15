""" Write a program to solve the knapsack problem where you can take an unlimited number of each item. """

def unbounded_knapsack(capacity, weights, values):
    n = len(values)
    
    dp = [0] * (capacity + 1)

    for w in range(capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

weights = [1, 3, 4]
values = [15, 50, 60] 
capacity = 8          

max_value = unbounded_knapsack(capacity, weights, values)
print("Maximum value in the knapsack:", max_value)
