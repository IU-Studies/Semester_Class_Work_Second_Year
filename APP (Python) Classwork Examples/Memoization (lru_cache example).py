from functools import lru_cache

@lru_cache(maxsize=None)  
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(50):
    print(fibonacci(i), end = " ")
