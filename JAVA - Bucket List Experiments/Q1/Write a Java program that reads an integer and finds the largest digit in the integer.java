// Write a Java program that reads an integer and finds the largest digit in the integer

import java.util.Scanner;

public class LargestDigitFinder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();
        
        number = Math.abs(number);

        int largestDigit = 0;

        while (number > 0) {
            int currentDigit = number % 10; 
            if (currentDigit > largestDigit) {
                largestDigit = currentDigit; 
            }
            number /= 10; 
        }

        System.out.println("Largest digit: " + largestDigit);
        scanner.close();
    }
}
