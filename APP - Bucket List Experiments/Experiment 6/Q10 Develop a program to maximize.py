""" Develop a program to maximize the value obtained by cutting a rod into various lengths based on given
prices for each length. """

def rod_cutting(prices, n):
    dp = [0] * (n + 1)

    for length in range(1, n + 1):
        for cut in range(1, length + 1):
            dp[length] = max(dp[length], prices[cut - 1] + dp[length - cut])

    return dp[n]

prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 8

max_profit = rod_cutting(prices, rod_length)
print("Maximum obtainable profit by cutting the rod:", max_profit)
