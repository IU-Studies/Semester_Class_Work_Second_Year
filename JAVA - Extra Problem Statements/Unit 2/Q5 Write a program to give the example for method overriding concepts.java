// Write a program to give the example for method overriding concepts. 

class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound.");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks.");
    }
}

public class MethodOverridingExample {
    public static void main(String[] args) {
        Animal myAnimal = new Animal(); 
        Animal myDog = new Dog();        

        myAnimal.makeSound(); 
        myDog.makeSound();    
    }
}
