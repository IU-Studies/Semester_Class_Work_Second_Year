""" Create a class Logger with a method log that prints a message before and after the execution of a
function. Use an instance of Logger as a decorator for a method compute in a class MathOperations.
Demonstrate by calling the decorated method.
Concepts Covered: Class-based Decorators """

class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Starting function:", self.func.__name__)
        result = self.func(*args, **kwargs)
        print("Finished function:", self.func.__name__)
        return result

class MathOperations:
    @Logger
    def compute(self, x, y):
        return x + y

math_op = MathOperations()

result = math_op.compute(10, 5)

print("Result of compute:", result)
