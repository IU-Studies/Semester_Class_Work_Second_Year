""" Define a class Counter with a method increment that increases a count by a specified value. Use a
decorator to print the current count before and after the increment operation. Implement a closure to
ensure the count is properly incremented within the method.
Concepts Covered: Class with Decorator and Closure """ 

def counter_decorator(func):
    def wrapper(self, value):
        print("Current count before increment:", self.count)
        result = func(self, value)  
        print("Current count after increment:", self.count)
        return result
    return wrapper

class Counter:
    def __init__(self):
        self.count = 0 

    @counter_decorator
    def increment(self, value):
        def adder():
            self.count += value
        adder()  
      
counter = Counter()
counter.increment(5)
counter.increment(10)
