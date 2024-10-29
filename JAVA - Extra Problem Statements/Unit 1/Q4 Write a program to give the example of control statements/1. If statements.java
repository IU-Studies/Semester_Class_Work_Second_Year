// Write a program to give the example of control statements.  
// If statements.

import java.util.Scanner;

public class ControlStatementExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();

        if (number > 0) {
            System.out.println("The number is positive.");
        }

        if (number < 0) {
            System.out.println("The number is negative.");
        }

        if (number == 0) {
            System.out.println("The number is zero.");
        }

        scanner.close();
    }
}
