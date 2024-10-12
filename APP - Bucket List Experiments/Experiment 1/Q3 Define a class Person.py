""" Define a class Person with a class variable population_count. Implement an __init__ method to
initialize a person’s name. Add a class method increment_population to increase population_count
whenever a new person is created. Demonstrate the usage of the class method by creating multiple
instances of Person.
Concepts Covered: Class Method, Class Variables """

class Person:
    population_count = 0

    def __init__(self, name):
        self.name = name
        Person.increment_population()

    def increment_population():
        Person.population_count += 1

person1 = Person("IU")
person2 = Person("UI")
person3 = Person("IM")

print("Population Count:", Person.population_count)
