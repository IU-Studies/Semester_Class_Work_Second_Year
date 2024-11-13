// Write a Java program to create an abstract class named Shape that contains two integers and an empty method named printArea(). 
// Provide three classes named Rectangle, Triangle, and Circle such that each one of the classes extends the class Shape. 
// Each one of the classes contains only the method printArea() that prints the area of the given shape (ABSTRACT CLASS).

abstract class Shape {
    int width;
    int height;

    public Shape(int width, int height) {
        this.width = width;
        this.height = height;
    }

    abstract void printArea();
}

class Rectangle extends Shape {
    public Rectangle(int width, int height) {
        super(width, height);
    }

    @Override
    void printArea() {
        int area = width * height;
        System.out.println("Area of Rectangle: " + area);
    }
}

class Triangle extends Shape {
    public Triangle(int width, int height) {
        super(width, height);
    }

    @Override
    void printArea() {
        double area = 0.5 * width * height;
        System.out.println("Area of Triangle: " + area);
    }
}

class Circle extends Shape {
    public Circle(int radius) {
        super(radius, 0); 
    }

    @Override
    void printArea() {
        double area = Math.PI * width * width; 
        System.out.println("Area of Circle: " + area);
    }
}

public class ShapeTest {
    public static void main(String[] args) {
        Shape rectangle = new Rectangle(5, 10);
        rectangle.printArea();

        Shape triangle = new Triangle(5, 10);
        triangle.printArea();

        Shape circle = new Circle(7);
        circle.printArea();
    }
}
