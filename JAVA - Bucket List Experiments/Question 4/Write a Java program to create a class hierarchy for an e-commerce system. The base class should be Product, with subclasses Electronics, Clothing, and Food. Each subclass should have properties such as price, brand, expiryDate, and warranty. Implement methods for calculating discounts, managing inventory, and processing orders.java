// Write a Java program to create a class hierarchy for an e-commerce system. 
// The base class should be Product, with subclasses Electronics, Clothing, and Food. 
// Each subclass should have properties such as price, brand, expiryDate, and warranty. 
// Implement methods for calculating discounts, managing inventory, and processing orders.

import java.util.Date;

class Product {
    private double price;
    private String brand;

    public Product(double price, String brand) {
        this.price = price;
        this.brand = brand;
    }

    public double getPrice() {
        return price;
    }

    public String getBrand() {
        return brand;
    }

    public double calculateDiscount(double discountPercentage) {
        return price - (price * discountPercentage / 100);
    }

    public void manageInventory() {
        System.out.println("Managing inventory for " + brand + " product.");
    }

    public void processOrder() {
        System.out.println("Processing order for " + brand + " product.");
    }
}

class Electronics extends Product {
    private int warranty; 

    public Electronics(double price, String brand, int warranty) {
        super(price, brand);
        this.warranty = warranty;
    }

    public void displayDetails() {
        System.out.println("Electronics Product:");
        System.out.println("Brand: " + getBrand());
        System.out.println("Price: $" + getPrice());
        System.out.println("Warranty: " + warranty + " months");
    }
}

class Clothing extends Product {
    private String size;

    public Clothing(double price, String brand, String size) {
        super(price, brand);
        this.size = size;
    }

    public void displayDetails() {
        System.out.println("Clothing Product:");
        System.out.println("Brand: " + getBrand());
        System.out.println("Price: $" + getPrice());
        System.out.println("Size: " + size);
    }
}

class Food extends Product {
    private Date expiryDate;

    public Food(double price, String brand, Date expiryDate) {
        super(price, brand);
        this.expiryDate = expiryDate;
    }

    public void displayDetails() {
        System.out.println("Food Product:");
        System.out.println("Brand: " + getBrand());
        System.out.println("Price: $" + getPrice());
        System.out.println("Expiry Date: " + expiryDate);
    }
}

public class ECommerceSystem {
    public static void main(String[] args) {
        Electronics electronics = new Electronics(299.99, "Samsung", 24);
        Clothing clothing = new Clothing(49.99, "Nike", "M");
        Food food = new Food(5.99, "Organic Farm", new Date());

        electronics.displayDetails();
        System.out.println("Discounted Price: $" + electronics.calculateDiscount(10));
        electronics.manageInventory();
        electronics.processOrder();
        
        System.out.println();

        clothing.displayDetails();
        System.out.println("Discounted Price: $" + clothing.calculateDiscount(15));
        clothing.manageInventory();
        clothing.processOrder();

        System.out.println();

        food.displayDetails();
        System.out.println("Discounted Price: $" + food.calculateDiscount(5));
        food.manageInventory();
        food.processOrder();
    }
}
