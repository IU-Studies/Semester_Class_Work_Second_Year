// In this program we will create a Binary Search Tree (BST).

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

public class BinarySearchTree {
    static Node insertIntoBST(Node root, int value) {
        if (root == null) {
            return new Node(value);
        }

        if (value > root.val) {
            root.right = insertIntoBST(root.right, value);
        } else {
            root.left = insertIntoBST(root.left, value);
        }

        return root;
    }

    static Node takeInput() {
        Scanner scanner = new Scanner(System.in);
        Node root = null;
        System.out.print("Enter data: ");
        int data = scanner.nextInt();

        while (data != -1) {
            root = insertIntoBST(root, data);
            data = scanner.nextInt();
        }
        return root;
    }

    public static void main(String[] args) {
        System.out.println("Enter data to create BST: ");
        Node root = takeInput();
    }
}
