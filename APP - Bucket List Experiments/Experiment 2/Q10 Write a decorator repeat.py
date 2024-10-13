""" Write a decorator repeat that takes a parameter times and repeats the execution of the decorated
function say_hello a specified number of times. Demonstrate the decorator by calling the say_hello
function with times set to 3.
Concepts Covered: Decorators with Parameters """

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)  
        return wrapper
    return decorator

@repeat(3)  
def say_hello():
    print("Hello!")

say_hello()
