import myPackage.Greeting;
import myPackage.Calculator;

public class Main {
    public static void main(String[] args) {
        Greeting greeting = new Greeting();
        greeting.displayGreeting();

        Calculator calculator = new Calculator();
        int sum = calculator.add(5, 3);
        int difference = calculator.subtract(5, 3);

        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
    }
}
