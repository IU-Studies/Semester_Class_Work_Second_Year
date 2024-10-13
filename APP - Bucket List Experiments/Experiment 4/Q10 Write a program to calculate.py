""" Write a program to calculate the nth Bell number, which represents the number of ways to partition
a set of n elements. """

def bell_number(n):
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    bell[0][0] = 1

    for i in range(1, n + 1):
        bell[i][0] = bell[i - 1][i - 1]

        for j in range(1, i + 1):
            bell[i][j] = bell[i][j - 1] + bell[i - 1][j - 1]

    return bell[n][0]

n = 5  
result = bell_number(n)
print("The ", str(n), "-th Bell number is: ", str(result))
