// Here in this program we will perform Preorder, Inorder, Postorder Traversal all at once.

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

public class BinaryTreeTraversals {
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

    static void preorder(Node root) {
        if (root == null) {
            return;
        }
        System.out.print(root.val + " ");
        preorder(root.left);
        preorder(root.right);
    }

    static void inorder(Node root) {
        if (root == null) {
            return;
        }
        inorder(root.left);
        System.out.print(root.val + " ");
        inorder(root.right);
    }

    static void postorder(Node root) {
        if (root == null) {
            return;
        }
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.val + " ");
    }

    public static void main(String[] args) {
        Node root = buildTree();

        System.out.println("Preorder Traversal is:");
        preorder(root);
        System.out.println();

        System.out.println("Inorder Traversal is:");
        inorder(root);
        System.out.println();

        System.out.println("Postorder Traversal is:");
        postorder(root);
        System.out.println();
    }
}
