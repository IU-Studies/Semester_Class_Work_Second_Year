// In this program we will perform postorder traversal on binary tree (non recursively) or we can say using stack

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int val;
    struct Node* left;
    struct Node* right;
};

struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->val = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct Node* BuildTree() {
    int data;
    printf("Enter data: ");
    scanf("%d", &data);

    if (data == -1) return NULL;

    struct Node* root = newNode(data);

    printf("Enter data in left of %d\n", data);
    root->left = BuildTree();

    printf("Enter data in right of %d\n", data);
    root->right = BuildTree();

    return root;
}

void Postorder(struct Node* root) {
    if (root == NULL) return;

    struct Node* stack[100]; 
    struct Node* lastVisited = NULL;
    struct Node* current = root;
    int top = -1;

    while (current != NULL || top != -1) {
        while (current != NULL) {
            stack[++top] = current;  
            current = current->left; 
        }

        current = stack[top];

        if (current->right != NULL && current->right != lastVisited) {
            current = current->right;
        } else {
            printf("%d ", current->val);
            lastVisited = current;
            current = NULL;
            top--;
        }
    }
}

int main() {
    struct Node* root = NULL;
    root = BuildTree();
    printf("Postorder Traversal: ");
    Postorder(root);
    return 0;
}
