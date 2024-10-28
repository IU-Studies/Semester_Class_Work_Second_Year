// Write a Java program that reads a string and counts the number of words in the string.

import java.util.Scanner;

public class WordCounter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a sentence: ");
        String input = scanner.nextLine().trim();

        if (input.isEmpty()) {
            System.out.println("The number of words is: 0");
        } else {
            String[] words = input.split("\\s+"); 
            System.out.println("The number of words is: " + words.length);
        }

        scanner.close();
    }
}
