// Write a program to arrange the numbers in ascending order. 

import java.util.Arrays;
import java.util.Scanner;

public class SortArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();

        int[] numbers = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }

        Arrays.sort(numbers); 

        System.out.println("Numbers in ascending order:");
        for (int number : numbers) {
            System.out.print(number + " ");
        }

        scanner.close();
    }
}
