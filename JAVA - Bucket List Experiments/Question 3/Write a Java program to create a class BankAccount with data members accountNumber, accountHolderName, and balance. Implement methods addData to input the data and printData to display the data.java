// Write a Java program to create a class BankAccount with data members accountNumber, accountHolderName, and balance. 
// Implement methods addData to input the data and printData to display the data.

import java.util.Scanner;

class BankAccount {
    String accountNumber;
    String accountHolderName;
    double balance;

    public void addData() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter account number: ");
        accountNumber = scanner.nextLine();

        System.out.print("Enter account holder name: ");
        accountHolderName = scanner.nextLine();

        System.out.print("Enter balance: ");
        balance = scanner.nextDouble();
    }

    public void printData() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Account Holder Name: " + accountHolderName);
        System.out.println("Balance: $" + balance);
    }
}

public class BankAccountDemo {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount();
        BankAccount account2 = new BankAccount();

        System.out.println("Enter data for Account 1:");
        account1.addData();

        System.out.println("\nEnter data for Account 2:");
        account2.addData();

        System.out.println("\nData of Account 1:");
        account1.printData();

        System.out.println("\nData of Account 2:");
        account2.printData();
    }
}
