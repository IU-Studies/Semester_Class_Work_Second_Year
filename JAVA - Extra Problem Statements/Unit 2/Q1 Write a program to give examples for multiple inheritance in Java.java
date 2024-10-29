// Write a program to give examples for multiple inheritance in Java. 

interface Vehicle {
    void start();
}

interface Machine {
    void operate();
}

class Car implements Vehicle, Machine {
    public void start() {
        System.out.println("Car is starting.");
    }

    public void operate() {
        System.out.println("Car is being operated.");
    }
}

public class MultipleInheritanceExample {
    public static void main(String[] args) {
        Car myCar = new Car();
        myCar.start();      
        myCar.operate();    
    }
}
