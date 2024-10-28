// Write a Java program to create an abstract class Appliance with properties like powerConsumption and brand, and an abstract method calculateEnergyUsage(). 
// Provide subclasses WashingMachine, Refrigerator, and Microwave, each implementing the calculateEnergyUsage() method to calculate energy usage based on their specific usage patterns.

abstract class Appliance {
    double powerConsumption; 
    String brand;            

    public Appliance(double powerConsumption, String brand) {
        this.powerConsumption = powerConsumption;
        this.brand = brand;
    }

    abstract double calculateEnergyUsage(int hoursUsed);
}

class WashingMachine extends Appliance {
    public WashingMachine(double powerConsumption, String brand) {
        super(powerConsumption, brand);
    }

    @Override
    double calculateEnergyUsage(int hoursUsed) {
        return powerConsumption * hoursUsed; 
    }
}

class Refrigerator extends Appliance {
    public Refrigerator(double powerConsumption, String brand) {
        super(powerConsumption, brand);
    }

    @Override
    double calculateEnergyUsage(int hoursUsed) {
        return powerConsumption * hoursUsed; 
    }
}

class Microwave extends Appliance {
    public Microwave(double powerConsumption, String brand) {
        super(powerConsumption, brand);
    }

    @Override
    double calculateEnergyUsage(int hoursUsed) {
        return powerConsumption * hoursUsed; 
    }
}

public class ApplianceTest {
    public static void main(String[] args) {
        Appliance washingMachine = new WashingMachine(500, "LG"); 
        System.out.println("Washing Machine Energy Usage: " + washingMachine.calculateEnergyUsage(2) + " watt-hours");

        Appliance refrigerator = new Refrigerator(150, "Samsung"); 
        System.out.println("Refrigerator Energy Usage: " + refrigerator.calculateEnergyUsage(24) + " watt-hours");

        Appliance microwave = new Microwave(1000, "Panasonic"); 
        System.out.println("Microwave Energy Usage: " + microwave.calculateEnergyUsage(0.5) + " watt-hours");
    }
}
