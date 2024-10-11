// In this program we will perform level order traversal or breadth first search (BFS) traversal on a binary tree

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

struct Node* BuildTree(struct Node* root) {
    int data;
    printf("Enter data: ");
    scanf("%d", &data);

    if (data == -1) return NULL;

    root = createNode(data);

    printf("Enter data in left of %d\n", data);
    root->left = BuildTree(root->left);

    printf("Enter data in right of %d\n", data);
    root->right = BuildTree(root->right);

    return root;
}

struct Queue {
    int front, rear;
    int size;
    struct Node* *array;
};

struct Queue* createQueue(int size) {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->front = queue->rear = -1;
    queue->size = size;
    queue->array = (struct Node**)malloc(queue->size * sizeof(struct Node*));
    return queue;
}

int isEmpty(struct Queue* queue) {
    return queue->front == -1;
}

void enqueue(struct Queue* queue, struct Node* item) {
    if (queue->rear == queue->size - 1) return;
    if (isEmpty(queue)) queue->front = 0;
    queue->array[++queue->rear] = item;
}

struct Node* dequeue(struct Queue* queue) {
    if (isEmpty(queue)) return NULL;
    struct Node* item = queue->array[queue->front];
    if (queue->front == queue->rear) queue->front = queue->rear = -1;
    else queue->front++;
    return item;
}

void LevelOrderTraversal(struct Node* root) {
    if (root == NULL) return;

    struct Queue* queue = createQueue(100); // Arbitrary queue size, adjust as needed
    enqueue(queue, root);

    while (!isEmpty(queue)) {
        struct Node* temp = dequeue(queue);
        printf("%d ", temp->val);

        if (temp->left) enqueue(queue, temp->left);
        if (temp->right) enqueue(queue, temp->right);
    }
    free(queue->array);
    free(queue);
}

int main() {
    struct Node* root = NULL;
    root = BuildTree(root);
    printf("Level Order Traversal: ");
    LevelOrderTraversal(root);
    return 0;
}
