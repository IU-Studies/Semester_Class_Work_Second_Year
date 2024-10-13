""" Write a program to determine how many distinct ways you can climb a staircase with n steps,
where you can take 1 or 2 steps at a time. """

def climb_stairs(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    ways = [0] * (n + 1)
    ways[0] = 1  
    ways[1] = 1  
    ways[2] = 2  

    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


n = 5  
result = climb_stairs(n)
print("Number of distinct ways to climb ", str(n) , " steps: " , str(result))
