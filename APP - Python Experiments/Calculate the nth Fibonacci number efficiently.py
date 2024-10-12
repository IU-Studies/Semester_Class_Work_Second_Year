def fibo(n):
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp

n = 15
print("Fibonacci Series till",n,"is as follows:")
print(fibo(n))
