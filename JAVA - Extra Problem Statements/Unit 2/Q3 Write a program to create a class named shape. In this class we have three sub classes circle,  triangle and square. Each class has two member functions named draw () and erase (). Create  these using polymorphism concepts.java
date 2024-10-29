// Write a program to create a class named shape. In this class we have three sub classes circle, 
// triangle and square. Each class has two member functions named draw () and erase (). 
// Create these using polymorphism concepts. 

class Shape {
    void draw() {
        System.out.println("Drawing a shape");
    }

    void erase() {
        System.out.println("Erasing a shape");
    }
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }

    @Override
    void erase() {
        System.out.println("Erasing a circle");
    }
}

class Triangle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a triangle");
    }

    @Override
    void erase() {
        System.out.println("Erasing a triangle");
    }
}

class Square extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a square");
    }

    @Override
    void erase() {
        System.out.println("Erasing a square");
    }
}

public class MainClass {
    public static void main(String[] args) {
        Shape shape;

        shape = new Circle();
        shape.draw();   
        shape.erase();  

        shape = new Triangle();
        shape.draw();   
        shape.erase();  

        shape = new Square();
        shape.draw();   
        shape.erase();  
    }
}
