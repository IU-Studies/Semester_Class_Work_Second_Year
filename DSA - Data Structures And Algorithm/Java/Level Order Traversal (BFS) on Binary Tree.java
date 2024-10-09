// In this program we will perform level order traversal or breadth first search (BFS) traversal on a binary tree.

import java.util.LinkedList;
import java.util.Queue;
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

    static void levelOrderTraversal(Node root) {
        if (root == null) {
            return;
        }

        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            Node temp = queue.poll();
            System.out.print(temp.val + " ");

            if (temp.left != null) {
                queue.add(temp.left);
            }
            if (temp.right != null) {
                queue.add(temp.right);
            }
        }
    }

    public static void main(String[] args) {
        Node root = buildTree();
        System.out.println("Level-order Traversal:");
        levelOrderTraversal(root);
    }
}
