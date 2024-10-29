// Write a program to calculate the following 
// Demonstrate a multidimensional array.

public class MultidimensionalArrayExample {
    public static void main(String[] args) {
        int[][][] multiArray = {
            {
                {1, 2, 3},
                {4, 5, 6}
            },
            {
                {7, 8, 9},
                {10, 11, 12}
            }
        };  

        System.out.println("Elements of the multidimensional array:");

        for (int i = 0; i < multiArray.length; i++) {
            for (int j = 0; j < multiArray[i].length; j++) {
                for (int k = 0; k < multiArray[i][j].length; k++) {
                    System.out.print(multiArray[i][j][k] + " ");  
                }
                System.out.println();  
            }
            System.out.println();  
        }
    }
}
