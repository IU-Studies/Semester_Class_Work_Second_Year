// In this program we will perform insertion at Kth position of linked list

#include <iostream>
using namespace std;

class Node{
public:
  int val;
  Node* next;

  Node (int data){
    val = data;
    next = NULL;
  }
};


void insertAtTail(Node* &head, int val){
  Node* new_node = new Node(val);
  Node* temp = head;
  while(temp->next != NULL){
    temp = temp->next;
  }
  temp->next = new_node;
}

void insertAtHead(Node* &head, int val){
  Node* new_node = new Node(val);
  new_node->next = head;
  head = new_node;
}

void insertAtK(Node* &head, int val, int pos){
    if (pos == 0){
      insertAtHead(head, val);
      return;
    }

    Node* new_node = new Node(val);
    Node* temp = head;
    int current_pos = 0;
    while (current_pos != pos-1){
      temp = temp->next;
      current_pos++;
    }

    new_node->next = temp->next;
    temp->next = new_node;
}
void display(Node* head){
  Node* temp = head;
  while (temp!=NULL){
    cout<<temp->val<<"->";
    temp = temp->next;
  }
  cout<<"NULL"<<endl;
}


int main(){

  Node* head = NULL;
  insertAtHead(head, 1);
  display(head);
  insertAtTail(head, 2);
  display(head);
  insertAtTail(head,3);
  display(head);
  insertAtTail(head,4);
  display(head);
  insertAtTail(head,5);
  display(head);
  insertAtK(head,323,2);
  display(head);

}
