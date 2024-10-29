// Write a java program that calculates the compound interest, taking the necessary input from the user.

import java.util.Scanner;

public class CompoundInterestCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the principal amount: ");
        double principal = scanner.nextDouble();

        System.out.print("Enter the annual interest rate (in %): ");
        double rate = scanner.nextDouble();

        System.out.print("Enter the time (in years): ");
        double time = scanner.nextDouble();

        System.out.print("Enter the number of times interest is compounded per year: ");
        int n = scanner.nextInt();

        double compoundInterest = principal * Math.pow(1 + (rate / 100) / n, n * time) - principal;

        System.out.println("Compound Interest: " + compoundInterest);
        System.out.println("Total Amount after " + time + " years: " + (principal + compoundInterest));

        scanner.close();
    }
}
