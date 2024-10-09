def feb(n):
    if n == 0:
        return 0
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

x = 100
for i in range(x + 1):
    print(feb(i))
