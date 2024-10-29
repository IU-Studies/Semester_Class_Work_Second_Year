// Create an outer class with a function display, again create another class inside the outer class 
// named inner with a function called display and call the two functions in the main class.

class Outer {
    void display() {
        System.out.println("Display from Outer class");
    }

    class Inner {
        void display() {
            System.out.println("Display from Inner class");
        }
    }
}

public class MainClass {
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.display(); 

        Outer.Inner inner = outer.new Inner();
        inner.display(); 
    }
}
