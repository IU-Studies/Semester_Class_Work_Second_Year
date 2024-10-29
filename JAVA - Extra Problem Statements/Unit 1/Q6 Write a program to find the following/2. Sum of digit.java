// Write a program to find the following 
// Sum of digit  

import java.util.Scanner;

public class SumOfDigits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();

        int sum = 0;

        number = Math.abs(number);

        while (number > 0) {
            sum += number % 10;  
            number /= 10;        
        }

        System.out.println("Sum of the digits: " + sum);

        scanner.close();
    }
}
