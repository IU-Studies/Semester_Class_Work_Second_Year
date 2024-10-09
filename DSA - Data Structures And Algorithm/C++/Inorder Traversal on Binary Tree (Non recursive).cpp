// In this program we will perform inorder traversal on binary tree (non recursively) or we can say using stack

#include <iostream>
using namespace std;

class Node {
public:
  int val;
  Node* left;
  Node* right;
    Node (int data){
      val = data;
      left = NULL;
      right = NULL;
    }
};

Node* BuildTree(Node* &root){
  int data;
  cout<<"Enter data:- ";
  cin>>data;

  if (data==-1) return NULL;

  root = new Node(data);

  cout<<"Enter data in left of "<<data<<endl;
  root->left = BuildTree(root->left);

  cout<<"Enter data in right of "<<data<<endl;
  root->right = BuildTree(root->right);

  return root;

}

class Stack{
public:
  Node* st[100];
  int top = -1;

  void push(Node* &root){
    st[++top] = root;
  }

  Node* pop(){
    return st[top--];
  }
};

void Inorder(Node* root) {    
  Stack s;  
  Node* current = root;

  while (current != NULL || s.top != -1) {
    while (current != NULL) {
      s.push(current);
      current = current->left;
    }
    current = s.pop();
    cout << current->val << " ";
    current = current->right;
  }
}


int main() {
  Node* root = NULL;
  BuildTree(root);
  cout<<"Inorder :- ";
  Inorder(root);
}
