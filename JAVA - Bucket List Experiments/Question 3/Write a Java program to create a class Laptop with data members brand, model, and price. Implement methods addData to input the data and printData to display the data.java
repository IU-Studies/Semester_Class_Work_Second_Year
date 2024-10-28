// Write a Java program to create a class Laptop with data members brand, model, and price. 
// Implement methods addData to input the data and printData to display the data.

import java.util.Scanner;

class Laptop {
    String brand;
    String model;
    double price;

    public void addData() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter brand: ");
        brand = scanner.nextLine();

        System.out.print("Enter model: ");
        model = scanner.nextLine();

        System.out.print("Enter price: ");
        price = scanner.nextDouble();
    }

    public void printData() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Price: $" + price);
    }
}

public class LaptopDemo {
    public static void main(String[] args) {
        Laptop laptop1 = new Laptop();
        Laptop laptop2 = new Laptop();

        System.out.println("Enter data for Laptop 1:");
        laptop1.addData();

        System.out.println("\nEnter data for Laptop 2:");
        laptop2.addData();

        System.out.println("\nData of Laptop 1:");
        laptop1.printData();

        System.out.println("\nData of Laptop 2:");
        laptop2.printData();
    }
}
