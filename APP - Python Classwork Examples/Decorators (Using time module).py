import time

def decorator(decorated_function):
    def decoration():
        start_time = time.time()
        print("Your program is starting...")
        decorated_function()
        end_time = time.time()
        print("Program ended, thank you!...")
        print("Execution time is:-", end_time - start_time)
    return decoration

@decorator
def hello():
    time.sleep(2)
    print("Hello this is a demo program...")

hello()
