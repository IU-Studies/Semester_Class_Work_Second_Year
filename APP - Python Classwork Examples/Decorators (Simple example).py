def decorator (decorated_function):
    def decoration():
        print("Your program is starting...")
        decorated_function()
        print("Program ended, thank you!...")
    return decoration

@decorator
def hello():
    print("Hello this is a demo program...")

hello()
