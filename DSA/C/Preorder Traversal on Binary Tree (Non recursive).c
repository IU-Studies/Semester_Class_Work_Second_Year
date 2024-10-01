// In this program we will perform preorder traversal on binary tree (non recursively) or we can say using stack

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

struct Stack {
    struct Node* st[100];
    int top;
};

void push(struct Stack* s, struct Node* node) {
    s->st[++(s->top)] = node;
}

struct Node* pop(struct Stack* s) {
    return s->st[(s->top)--];
}

void Preorder(struct Node* root) {
    struct Stack s;
    s.top = -1; 
    if (root == NULL) return;

    push(&s, root);

    while (s.top != -1) {
        root = pop(&s); 
        printf("%d ", root->val);

        if (root->right != NULL) push(&s, root->right);
        if (root->left != NULL) push(&s, root->left);
    }
}

int main() {
    struct Node* root = NULL;
    root = BuildTree();
    printf("Preorder Traversal: ");
    Preorder(root);
    return 0;
}
