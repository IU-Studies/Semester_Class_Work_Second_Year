// Write a Java program that creates a class hierarchy for employees of a company. 
// The base class should be Employee, with subclasses Manager, Developer, and Programmer. 
// Each subclass should have properties such as name, address, salary, and jobTitle. 
// Implement methods for calculating bonuses, generating performance reports, and managing projects. (ENCAPSULATION)

class Employee {
    private String name;
    private String address;
    private double salary;
    private String jobTitle;

    public Employee(String name, String address, double salary, String jobTitle) {
        this.name = name;
        this.address = address;
        this.salary = salary;
        this.jobTitle = jobTitle;
    }

    public double calculateBonus() {
        return salary * 0.10; 
    }

    public String generatePerformanceReport() {
        return "Performance report for " + name + " (Job Title: " + jobTitle + "):\n"
                + "Salary: $" + salary + "\n"
                + "Bonus: $" + calculateBonus();
    }

    public String getName() {
        return name;
    }
}

class Manager extends Employee {
    public Manager(String name, String address, double salary) {
        super(name, address, salary, "Manager");
    }

    @Override
    public double calculateBonus() {
        return super.calculateBonus() + 500; 
    }
}

class Developer extends Employee {
    public Developer(String name, String address, double salary) {
        super(name, address, salary, "Developer");
    }
}

class Programmer extends Employee {
    public Programmer(String name, String address, double salary) {
        super(name, address, salary, "Programmer");
    }
}

public class EmployeeDemo {
    public static void main(String[] args) {
        Employee manager = new Manager("Alice Smith", "123 Main St", 80000);
        Employee developer = new Developer("Bob Johnson", "456 Elm St", 60000);
        Employee programmer = new Programmer("Charlie Brown", "789 Oak St", 70000);

        System.out.println(manager.generatePerformanceReport());
        System.out.println();
        System.out.println(developer.generatePerformanceReport());
        System.out.println();
        System.out.println(programmer.generatePerformanceReport());
    }
}
