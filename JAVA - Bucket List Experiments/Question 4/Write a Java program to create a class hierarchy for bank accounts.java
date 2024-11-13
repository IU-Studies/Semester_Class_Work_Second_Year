// Write a Java program to create a class hierarchy for bank accounts. 
// The base class should be Account, with subclasses SavingsAccount, CheckingAccount, and FixedDepositAccount. 
// Each subclass should have properties such as accountNumber, balance, interestRate, and accountHolderName. 
// Implement methods for calculating interest, managing transactions, and generating account statements.

class Account {
    protected String accountNumber;
    protected double balance;
    protected String accountHolderName;

    public Account(String accountNumber, double initialBalance, String accountHolderName) {
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
        this.accountHolderName = accountHolderName;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: $" + amount);
        } else {
            System.out.println("Invalid deposit amount.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount);
        } else {
            System.out.println("Invalid withdrawal amount.");
        }
    }

    public double getBalance() {
        return balance;
    }

    public String getAccountStatement() {
        return "Account Number: " + accountNumber + "\nAccount Holder: " + accountHolderName + "\nBalance: $" + balance;
    }
}

class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount(String accountNumber, double initialBalance, String accountHolderName, double interestRate) {
        super(accountNumber, initialBalance, accountHolderName);
        this.interestRate = interestRate;
    }

    public void calculateInterest() {
        double interest = balance * interestRate / 100;
        balance += interest;
        System.out.println("Interest calculated: $" + interest);
    }

    @Override
    public String getAccountStatement() {
        return super.getAccountStatement() + "\nInterest Rate: " + interestRate + "%";
    }
}

class CheckingAccount extends Account {
    public CheckingAccount(String accountNumber, double initialBalance, String accountHolderName) {
        super(accountNumber, initialBalance, accountHolderName);
    }

    @Override
    public String getAccountStatement() {
        return super.getAccountStatement() + "\nAccount Type: Checking Account";
    }
}

class FixedDepositAccount extends Account {
    private double interestRate;
    private int tenure; // in months

    public FixedDepositAccount(String accountNumber, double initialBalance, String accountHolderName, double interestRate, int tenure) {
        super(accountNumber, initialBalance, accountHolderName);
        this.interestRate = interestRate;
        this.tenure = tenure;
    }

    public void calculateMaturityAmount() {
        double maturityAmount = balance + (balance * interestRate / 100 * tenure / 12);
        System.out.println("Maturity Amount after " + tenure + " months: $" + maturityAmount);
    }

    @Override
    public String getAccountStatement() {
        return super.getAccountStatement() + "\nInterest Rate: " + interestRate + "%\nTenure: " + tenure + " months";
    }
}

public class BankSystem {
    public static void main(String[] args) {
        SavingsAccount savingsAccount = new SavingsAccount("SA123", 1000, "Alice", 5);
        savingsAccount.deposit(500);
        savingsAccount.calculateInterest();
        System.out.println(savingsAccount.getAccountStatement());

        System.out.println();

        CheckingAccount checkingAccount = new CheckingAccount("CA456", 2000, "Bob");
        checkingAccount.withdraw(300);
        System.out.println(checkingAccount.getAccountStatement());

        System.out.println();

        FixedDepositAccount fixedDepositAccount = new FixedDepositAccount("FD789", 1500, "Charlie", 6, 12);
        fixedDepositAccount.calculateMaturityAmount();
        System.out.println(fixedDepositAccount.getAccountStatement());
    }
}
