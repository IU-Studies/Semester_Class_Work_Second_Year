""" Implement a generator function fibonacci_gen that yields Fibonacci numbers up to a specified limit.
Use this generator to print the Fibonacci numbers up to 100.
Concepts Covered: Generators """

def fibonacci_gen(limit):
    a, b = 0, 1
    while a <= limit:
        yield a  
        a, b = b, a + b  

for number in fibonacci_gen(100):
    print(number)
