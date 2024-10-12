"""Create a class Calculator with two instance variables a and b. Implement instance methods to
perform addition and subtraction. Add a static method to multiply two numbers without using the
instance variables. Create an object of Calculator and demonstrate the usage of instance and static
methods.
Concepts Covered: Instance Methods, Static Methods"""

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self, x, y):
        return x * y

calc = Calculator(10, 5)

print("Addition:", calc.add())        
print("Subtraction:", calc.subtract()) 
print("Multiplication:", calc.multiply(4, 3)) 
