// Write a Java program to create a class Product with data members productName, category, and price. 
// Implement methods addData to input the data and printData to display the data.

import java.util.Scanner;

class Product {
    String productName;
    String category;
    double price;

    public void addData() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter product name: ");
        productName = scanner.nextLine();

        System.out.print("Enter category: ");
        category = scanner.nextLine();

        System.out.print("Enter price: ");
        price = scanner.nextDouble();
    }

    public void printData() {
        System.out.println("Product Name: " + productName);
        System.out.println("Category: " + category);
        System.out.println("Price: $" + price);
    }
}

public class ProductDemo {
    public static void main(String[] args) {
        Product p1 = new Product();
        Product p2 = new Product();

        System.out.println("Enter data for Product 1:");
        p1.addData();

        System.out.println("\nEnter data for Product 2:");
        p2.addData();

        System.out.println("\nData of Product 1:");
        p1.printData();

        System.out.println("\nData of Product 2:");
        p2.printData();
    }
}
