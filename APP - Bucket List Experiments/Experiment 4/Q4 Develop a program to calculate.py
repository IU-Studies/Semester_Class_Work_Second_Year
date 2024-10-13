""" Develop a program to calculate the nth Catalan number, which appears in various combinatorial problems. """

def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def catalan_number(n):
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))

n = 5  
result = catalan_number(n)
print("The ", str(n), "th Catalan number is: ", str(result))
