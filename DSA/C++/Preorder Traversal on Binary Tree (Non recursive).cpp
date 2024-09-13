// In this program we will perform preorder traversal on binary tree (non recursively) or we can say using stack

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

void Preorder(Node* &root){
  Stack s;
  if (root==NULL) return;
  s.push(root);

  while (s.top != -1){
    root = s.pop();
    cout<<root->val<<" ";
    if (root->right != NULL) s.push(root->right);
    if (root->left != NULL) s.push(root->left);
  }
}


int main() {
  Node* root = NULL;
  BuildTree(root);
  Preorder(root);
}
