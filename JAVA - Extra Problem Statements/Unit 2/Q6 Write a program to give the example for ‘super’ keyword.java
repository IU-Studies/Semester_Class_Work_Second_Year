// Write a program to give the example for ‘super’ keyword

class Animal {
    String name;

    Animal(String name) {
        this.name = name;
    }

    void display() {
        System.out.println("Animal Name: " + name);
    }
}

class Dog extends Animal {
    String breed;

    Dog(String name, String breed) {
        super(name); 
        this.breed = breed;
    }

    void display() {
        super.display(); 
        System.out.println("Dog Breed: " + breed);
    }
}

public class SuperKeywordExample {
    public static void main(String[] args) {
        Dog myDog = new Dog("Buddy", "Golden Retriever");
        myDog.display();
    }
}
