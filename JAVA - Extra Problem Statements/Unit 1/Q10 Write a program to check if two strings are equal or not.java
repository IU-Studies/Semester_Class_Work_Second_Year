// Write a program to check if two strings are equal or not. 

import java.util.Scanner;

public class StringEqualityCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first string: ");
        String firstString = scanner.nextLine();

        System.out.print("Enter the second string: ");
        String secondString = scanner.nextLine();

        if (firstString.equals(secondString)) {
            System.out.println("The strings are equal.");
        } else {
            System.out.println("The strings are not equal.");
        }

        scanner.close();
    }
}
