// Create a class named ‘a’ and create a sub class ‘b’. Which extends from class ‘a’. And use these 
// classes in the ‘inherit’ class. 

class A {
    void displayA() {
        System.out.println("This is class A.");
    }
}

class B extends A {
    void displayB() {
        System.out.println("This is class B, which extends class A.");
    }
}

public class Inherit {
    public static void main(String[] args) {
        A objA = new A();
        objA.displayA();

        B objB = new B();
        objB.displayA(); 
        objB.displayB(); 
    }
}
