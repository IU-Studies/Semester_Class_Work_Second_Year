// Write a program to calculate the following 
// Demonstrate a one-dimensional array.

public class OneDimensionalArrayExample {
    public static void main(String[] args) {
        int[] numbers = {5, 10, 15, 20, 25};  

        System.out.println("Elements of the one-dimensional array:");

        for (int i = 0; i < numbers.length; i++) {
            System.out.println("Element at index " + i + ": " + numbers[i]);
        }
    }
}
