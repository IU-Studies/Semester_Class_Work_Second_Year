# c. Showcase how inheritance facilitates code organization and promotes code reusability. 

# Animal Class Hierarchy

This project demonstrates the use of inheritance in object-oriented programming through a class hierarchy representing different types of animals.

## Overview

The project consists of three main subclasses of the base `Animal` class: `Mammal`, `Bird`, and `Fish`. Each subclass extends the functionality of the base class while adding specific properties and methods relevant to each animal type.

### Animal Class

The `Animal` class serves as the base class and includes:
- **Properties**: `name`, `age`
- **Methods**:
  - `eat()`: Common method for all animals.
  - `sleep()`: Common method for all animals.

### Mammal Class

The `Mammal` class extends the `Animal` class and adds:
- **Property**: `hasFur`
- **Methods**:
  - `giveBirth()`: Method specific to mammals.
  - `displayInfo()`: Displays information about the mammal.

### Bird Class

The `Bird` class extends the `Animal` class and adds:
- **Property**: `canFly`
- **Methods**:
  - `layEggs()`: Method specific to birds.
  - `displayInfo()`: Displays information about the bird.

### Fish Class

The `Fish` class extends the `Animal` class and adds:
- **Property**: `isSaltwater`
- **Methods**:
  - `swim()`: Method specific to fish.
  - `displayInfo()`: Displays information about the fish.

## Main Class

The main class creates instances of `Mammal`, `Bird`, and `Fish`, demonstrating the use of inheritance by calling their respective methods. This showcases how specific functionality can be implemented in subclasses while reusing common functionality from the `Animal` class.

## Benefits of Inheritance

- **Code Reusability**: Common attributes and methods are defined in the `Animal` base class, reducing code duplication in the subclasses.
- **Organization**: The class hierarchy clearly defines relationships among different types of animals, making the code more organized and easier to understand.
- **Extensibility**: New animal types can be easily added by creating new subclasses that inherit from the `Animal` class.
