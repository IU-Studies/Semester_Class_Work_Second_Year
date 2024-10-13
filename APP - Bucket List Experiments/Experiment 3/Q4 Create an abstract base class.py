""" Create an abstract base class Animal with a method make_sound. Implement two concrete classes
Dog and Cat that inherit from Animal and override make_sound. Define an AnimalFactory with a
method create_animal to return Dog or Cat instances based on input. Demonstrate the factory in
action.
Concepts Covered: Factory Pattern with Abstract Base Class """

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            raise ValueError("Unknown animal type")

factory = AnimalFactory()

dog = factory.create_animal('dog')
print("Dog sound:", dog.make_sound())

cat = factory.create_animal('cat')
print("Cat sound:", cat.make_sound())
