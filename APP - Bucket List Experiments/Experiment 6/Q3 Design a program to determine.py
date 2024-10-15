""" Design a program to determine the minimum number of coins needed to make a specific amount of
money from a given set of coin denominations. """

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
          
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]  
amount = 11        

min_coins = coin_change(coins, amount)
print("Minimum number of coins needed:", min_coins)
