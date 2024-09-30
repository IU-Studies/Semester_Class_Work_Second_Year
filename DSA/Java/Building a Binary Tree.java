// In this program we will be creating a basic binary tree
// Input -1 to stop taking inputs.

import java.util.Scanner;

class Node {
    int val;
    Node left, right;

    Node(int data) {
        val = data;
        left = null;
        right = null;
    }
}

public class BinaryTree {
    static Node buildTree() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter data (-1 to stop): ");
        int data = scanner.nextInt();

        if (data == -1) {
            return null;
        }

        Node root = new Node(data);

        System.out.println("Enter data in left of " + data);
        root.left = buildTree();

        System.out.println("Enter data in right of " + data);
        root.right = buildTree();

        return root;
    }

    public static void main(String[] args) {
        Node root = buildTree();
    }
}
