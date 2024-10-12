""" Create a base class Shape with a method draw(). Define two derived classes, Circle and Square,
each implementing the draw() method in their own way. Create a list of Shape objects and call the
draw() method on each object to demonstrate polymorphism.
Concepts Covered: Polymorphism, Method Overriding """ 

class Shape:
    def draw(self):
        pass
    
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

shapes = [Circle(), Square(), Circle()]

for shape in shapes:
    shape.draw()
