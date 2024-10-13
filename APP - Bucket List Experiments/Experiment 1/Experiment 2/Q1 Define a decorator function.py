""" Define a decorator function add_10 that adds 10 to the result of the function it decorates. Use this
decorator on a function get_number that returns a number. Demonstrate the usage by calling the
decorated function and printing the result.
Concepts Covered: Decorators """

def add_10(func):
    def wrapper():
        result = func()  
        return result + 10  
    return wrapper

@add_10
def get_number():
    return 5  

result = get_number()
print(result)  
