// In this program we will perform deletion at Kth position of linked list

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

void deleteAtHead(Node* &head){
  Node* temp = head;
  head = head->next;
  free(temp);
}

void deleteAtKPos(Node* &head, int pos){
  if (pos == 0){ 
    deleteAtHead(head);
    return;
  }
  int curr_pos = 0;
  Node* prev = head;
  while (curr_pos != pos-1){
    prev = prev->next;
    curr_pos++;
  }

  Node* temp = prev->next;
  prev->next = prev->next->next;
  free(temp);
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
  deleteAtKPos(head, 2);
  display(head);

}
