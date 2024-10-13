""" Define a VehicleFactory class with a method create_vehicle that creates Car or Bike objects based
on input parameters (e.g., type). Implement Car and Bike classes with a drive method. Demonstrate
creating and using vehicles based on factory parameters.
Concepts Covered: Factory Pattern with Parameters """

class Vehicle:
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car!"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike!"

class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'bike':
            return Bike()
        else:
            raise ValueError("Unknown vehicle type")

factory = VehicleFactory()

car = factory.create_vehicle('car')
print(car.drive())  

bike = factory.create_vehicle('bike')
print(bike.drive())  

try:
    unknown_vehicle = factory.create_vehicle('truck')
except ValueError as e:
    print(e)  
