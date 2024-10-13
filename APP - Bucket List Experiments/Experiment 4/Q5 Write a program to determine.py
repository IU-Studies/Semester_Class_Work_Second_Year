""" Write a program to determine the number of ways to tile a 2 x n board using 2 x 1 tiles. """

def count_tiling_ways(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
      
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
  
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

n = 5  
result = count_tiling_ways(n)
print("Number of ways to tile a 2 x ", str(n), " board: ", str(result))
