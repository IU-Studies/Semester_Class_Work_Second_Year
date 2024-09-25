// In this program we will create a Binary Search Tree (BST).

#include <iostream>
using namespace std;

class Node{
public:
  int val;
  Node* left;
  Node* right;
  Node(int data){
    val = data;
    left = NULL;
    right = NULL;
  }
};

Node* insertIntoBST(Node* root, int value){
  
  if (root == NULL) {
    root = new Node(value);
    return root;
  }
  
  if (value > root->val) root->right = insertIntoBST(root->right, value);

  else root->left = insertIntoBST(root->left, value);

  return root;
  
}

void TakeInput(Node* &root){
  int data;
  cin>>data;
  while (data != -1){
    root = insertIntoBST(root, data);
    cin>>data;
  }
}


int main() {
  
  Node* root = NULL;
  cout<<"Enter data:- ";
  TakeInput(root);
  
}
