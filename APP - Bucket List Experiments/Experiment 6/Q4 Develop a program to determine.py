""" Develop a program to determine the maximum profit obtainable by cutting a rod of a given length into
pieces with given values. """

def rod_cutting(prices, length):
    dp = [0] * (length + 1)

    for i in range(1, length + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j - 1] + dp[i - j])

    return dp[length]

prices = [1, 5, 8, 9, 10, 17, 17, 20]
length = 8

max_profit = rod_cutting(prices, length)
print("Maximum profit obtainable:", max_profit)
