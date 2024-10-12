""" Define a class Engine with attributes horsepower and type. Create a class Car that contains an
Engine object as an attribute. Implement methods in Car to get engine details and display car details
along with engine details.
Concepts Covered: Composition """ 

class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type

    def get_engine_details(self):
        return "Horsepower: " + str(self.horsepower) + ", Type: " + self.engine_type


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def display_details(self):
        engine_details = self.engine.get_engine_details()  
        return "Car Make: " + self.make + ", Model: " + self.model + ", Engine: (" + engine_details + ")"

engine = Engine(250, "V8")

car = Car("Ford", "Mustang", engine)

print(car.display_details())
