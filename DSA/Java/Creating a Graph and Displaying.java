import java.util.Scanner;

public class GraphInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of vertices: ");
        int n = sc.nextInt();

        int[][] graph = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("Point " + (char)(65 + i) + " to " + (char)(65 + j) + " : ");
                graph[i][j] = sc.nextInt();
            }
        }

        System.out.println("Adjacency Matrix: ");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
        
        sc.close();
    }
}
