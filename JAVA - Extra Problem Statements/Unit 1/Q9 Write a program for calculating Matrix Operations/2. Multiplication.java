// Write a program for calculating Matrix Operations
// Multiplication

import java.util.Scanner;

public class MatrixMultiplication {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of rows for Matrix A: ");
        int rowsA = scanner.nextInt();
        System.out.print("Enter the number of columns for Matrix A (and rows for Matrix B): ");
        int columnsA = scanner.nextInt();
        System.out.print("Enter the number of columns for Matrix B: ");
        int columnsB = scanner.nextInt();

        int[][] matrixA = new int[rowsA][columnsA];
        int[][] matrixB = new int[columnsA][columnsB];
        int[][] productMatrix = new int[rowsA][columnsB];

        System.out.println("Enter elements of Matrix A:");
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < columnsA; j++) {
                matrixA[i][j] = scanner.nextInt();
            }
        }

        System.out.println("Enter elements of Matrix B:");
        for (int i = 0; i < columnsA; i++) {
            for (int j = 0; j < columnsB; j++) {
                matrixB[i][j] = scanner.nextInt();
            }
        }

        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < columnsB; j++) {
                for (int k = 0; k < columnsA; k++) {
                    productMatrix[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        System.out.println("Product of Matrix A and Matrix B:");
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < columnsB; j++) {
                System.out.print(productMatrix[i][j] + " ");
            }
            System.out.println();
        }

        scanner.close();
    }
}
