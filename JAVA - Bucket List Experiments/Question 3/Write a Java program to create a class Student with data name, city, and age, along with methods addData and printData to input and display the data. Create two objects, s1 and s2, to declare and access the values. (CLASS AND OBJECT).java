// Write a Java program to create a class Student with data name, city, and age, 
// along with methods addData and printData to input and display the data. Create two objects, 
// s1 and s2, to declare and access the values. (CLASS AND OBJECT)

import java.util.Scanner;

class Student {
    String name;
    String city;
    int age;

    public void addData() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter name: ");
        name = scanner.nextLine();

        System.out.print("Enter city: ");
        city = scanner.nextLine();

        System.out.print("Enter age: ");
        age = scanner.nextInt();
    }

    public void printData() {
        System.out.println("Name: " + name);
        System.out.println("City: " + city);
        System.out.println("Age: " + age);
    }
}

public class StudentDemo {
    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student();

        System.out.println("Enter data for Student 1:");
        s1.addData();

        System.out.println("\nEnter data for Student 2:");
        s2.addData();

        System.out.println("\nData of Student 1:");
        s1.printData();

        System.out.println("\nData of Student 2:");
        s2.printData();
    }
}
