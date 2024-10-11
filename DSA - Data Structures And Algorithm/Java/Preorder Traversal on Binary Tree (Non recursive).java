// In this program we will perform preorder traversal on binary tree (non recursively) or we can say using stack

import java.util.Stack;
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

    static Node buildTree(Scanner sc) {
        System.out.print("Enter data: ");
        int data = sc.nextInt();

        if (data == -1) return null;

        Node root = new Node(data);

        System.out.println("Enter data in left of " + data);
        root.left = buildTree(sc);

        System.out.println("Enter data in right of " + data);
        root.right = buildTree(sc);

        return root;
    }

    static void preorder(Node root) {
        if (root == null) return;

        Stack<Node> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()) {
            Node current = stack.pop();
            System.out.print(current.val + " ");

            // Push right child first so that left child is processed first
            if (current.right != null) stack.push(current.right);
            if (current.left != null) stack.push(current.left);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node root = null;

        root = buildTree(sc);

        System.out.print("Preorder: ");
        preorder(root);
    }
}
