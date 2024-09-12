def decorator(decorated_function):
    def decoration(*args, **kwargs):
        print("Your program is starting...")
        decorated_function(*args, **kwargs)
        print("Program ended, thank you!...")
    return decoration

@decorator
def add_two_numbers(num1, num2):
    result = num1 + num2
    print("Result is :-", result)

add_two_numbers(10, 20)
