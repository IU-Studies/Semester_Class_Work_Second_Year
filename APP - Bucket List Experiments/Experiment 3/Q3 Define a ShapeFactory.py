""" Define a ShapeFactory class with a method create_shape that returns different shape objects
(Circle or Square) based on the input string. Implement Circle and Square classes with a method
draw that prints the shape name. Demonstrate creating and drawing shapes using the factory.
Concepts Covered: Factory Pattern """ 

class Circle:
    def draw(self):
        print("Drawing a Circle")

class Square:
    def draw(self):
        print("Drawing a Square")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "square":
            return Square()
        else:
            raise ValueError("Unknown shape type: " + shape_type)

shape1 = ShapeFactory.create_shape("circle")
shape1.draw()  

shape2 = ShapeFactory.create_shape("square")
shape2.draw()  

try:
    shape3 = ShapeFactory.create_shape("triangle")
    shape3.draw()
except ValueError as e:
    print(e)  
