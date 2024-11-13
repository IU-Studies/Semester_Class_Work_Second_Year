// Write a Java program to create an abstract class Vehicle that contains properties like speed and fuelCapacity, and an abstract method calculateRange(). 
// Provide subclasses Car, Motorcycle, and Truck, each implementing the calculateRange() method to calculate the range based on their specific fuel efficiency.

abstract class Vehicle {
    int speed;          
    int fuelCapacity;   

    public Vehicle(int speed, int fuelCapacity) {
        this.speed = speed;
        this.fuelCapacity = fuelCapacity;
    }
  
    abstract double calculateRange();
}

class Car extends Vehicle {
    double fuelEfficiency; 

    public Car(int speed, int fuelCapacity, double fuelEfficiency) {
        super(speed, fuelCapacity);
        this.fuelEfficiency = fuelEfficiency;
    }

    @Override
    double calculateRange() {
        return fuelEfficiency * fuelCapacity;
    }
}

class Motorcycle extends Vehicle {
    double fuelEfficiency; 

    public Motorcycle(int speed, int fuelCapacity, double fuelEfficiency) {
        super(speed, fuelCapacity);
        this.fuelEfficiency = fuelEfficiency;
    }

    @Override
    double calculateRange() {
        return fuelEfficiency * fuelCapacity;
    }
}

class Truck extends Vehicle {
    double fuelEfficiency; 

    public Truck(int speed, int fuelCapacity, double fuelEfficiency) {
        super(speed, fuelCapacity);
        this.fuelEfficiency = fuelEfficiency;
    }

    @Override
    double calculateRange() {
        return fuelEfficiency * fuelCapacity;
    }
}

public class VehicleTest {
    public static void main(String[] args) {
        Vehicle car = new Car(120, 50, 15.0); 
        System.out.println("Car range: " + car.calculateRange() + " km");

        Vehicle motorcycle = new Motorcycle(100, 15, 30.0); 
        System.out.println("Motorcycle range: " + motorcycle.calculateRange() + " km");

        Vehicle truck = new Truck(80, 150, 5.0); 
        System.out.println("Truck range: " + truck.calculateRange() + " km");
    }
}
