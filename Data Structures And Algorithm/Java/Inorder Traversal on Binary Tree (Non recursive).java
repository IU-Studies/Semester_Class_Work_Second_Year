// In this program we will perform inorder traversal on binary tree (non recursively) or we can say using stack.

import java.util.Scanner;
import java.util.Stack;

class Node {
    int val;
    Node left, right;

    Node(int data) {
        val = data;
        left = null;
        right = null;
    }
}

public class InorderTraversalNonRecursive {

    static Node buildTree() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter data : ");
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

    static void inorder(Node root) {
        if (root == null) {
            return;
        }

        Stack<Node> stack = new Stack<>();
        Node current = root;

        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            System.out.print(current.val + " ");

            current = current.right;
        }
    }

    public static void main(String[] args) {
        Node root = buildTree();

        System.out.println("Inorder Traversal is:");
        inorder(root);
        System.out.println();
    }
}
