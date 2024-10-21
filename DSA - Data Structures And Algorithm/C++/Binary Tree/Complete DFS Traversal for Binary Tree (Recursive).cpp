// Here in this program we will perform Preorder, Inorder, Postorder Traversal all at once.

#include <iostream>
using namespace std;

class Node{
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
  root = new Node(data);
  if (data == -1) return NULL;

  cout<<"Enter data in left of "<<data<<endl;
  root->left = BuildTree(root->left);
  
  cout<<"Enter data in right of "<<data<<endl;
  root->right = BuildTree(root->right);

  return root;
}

void Preorder(Node* &root){
  if (root==NULL) return;
  cout<<root->val<<" ";
  Preorder(root->left);
  Preorder(root->right);
}

void Inorder(Node* &root){
  if (root==NULL) return;
  Inorder(root->left);
  cout<<root->val<<" ";
  Inorder(root->right);
}

void Postorder(Node* &root){
  if (root==NULL) return;
  Postorder(root->left);
  Postorder(root->right);
  cout<<root->val<<" ";
}

int main(){
  Node* root = NULL;
  BuildTree(root);
  
  cout<<"Preorder Traversal is:- ";
  Preorder(root);
  cout<<endl;
  
  cout<<"Inorder Traversal is:- ";
  Inorder(root);
  cout<<endl;
  
  cout<<"Postorder Traversal is:- ";
  Postorder(root);
  cout<<endl;
}
