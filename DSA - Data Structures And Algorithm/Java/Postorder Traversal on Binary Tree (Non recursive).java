// In this program we will perform postorder traversal on binary tree (non recursively) or we can say using stack

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

    static void postOrderTraversal(Node root) {
        if (root == null) {
            return;
        }

        Stack<Node> stack = new Stack<>();
        Node lastVisited = null;
        Node current = root;

        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.peek();

            if (current.right != null && current.right != lastVisited) {
                current = current.right;
            } else {
                System.out.print(current.val + " ");
                lastVisited = current;
                stack.pop();
                current = null;
            }
        }
    }

    public static void main(String[] args) {
        Node root = buildTree();
        System.out.println("Post-order Traversal:");
        postOrderTraversal(root);
    }
}
