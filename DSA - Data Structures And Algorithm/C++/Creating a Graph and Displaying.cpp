// In this program we will create a graph and display it.

#include <iostream>
using namespace std;

int main(){
  int n;
  cout<<"Enter no. of vertices:- ";
  cin>>n;
  int graph[n][n];

  for (int i=0; i<n; i++){
    for (int j=0; j<n; j++){
      cout<<"Point "<<static_cast<char>(65 + i)<<" to "<<static_cast<char>(65 + j)<<":-";
      cin>>graph[i][j];
    }
  }
  
  for (int i=0; i<n; i++){
    for (int j=0; j<n; j++){
      cout<<graph[i][j]<<" ";
    }
    cout<<endl;
}
  
}
