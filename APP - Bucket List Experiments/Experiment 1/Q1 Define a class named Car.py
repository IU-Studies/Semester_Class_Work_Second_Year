"""Define a class named Car with attributes make, model, and year. Create a constructor to initialize
these attributes. Create an instance of Car and display its attributes.
Concepts Covered: Class, Object, Constructor, Instance Variables"""

class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

my_car = Car("BMW", "Class", 2000)

print(my_car.company)
print(my_car.model)
print(my_car.year)
