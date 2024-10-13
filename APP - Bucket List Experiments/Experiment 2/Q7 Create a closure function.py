""" Create a closure function make_multiplier that takes a number n and returns a function that
multiplies its input by n. Test this closure by creating a multiplier function for doubling and tripling
values, and demonstrate its usage.
Concepts Covered: Closures """

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

doubler = make_multiplier(2)

tripler = make_multiplier(3)

print(doubler(5))  
print(tripler(5))  
