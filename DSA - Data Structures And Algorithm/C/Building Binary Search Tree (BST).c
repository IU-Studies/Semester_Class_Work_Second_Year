// In this program we will create a Binary Search Tree (BST).

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int val;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->val = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

struct Node* insertIntoBST(struct Node* root, int value) {
    if (root == NULL) {
        root = createNode(value);
        return root;
    }
    
    if (value > root->val) 
        root->right = insertIntoBST(root->right, value);
    else 
        root->left = insertIntoBST(root->left, value);
    
    return root;
}

void TakeInput(struct Node** root) {
    int data;
    scanf("%d", &data);
    while (data != -1) {
        *root = insertIntoBST(*root, data);
        scanf("%d", &data);
    }
}

int main() {
    struct Node* root = NULL;
    printf("Enter data (-1 to stop): ");
    TakeInput(&root);
    
    return 0;
}
