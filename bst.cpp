#include<iostream>
using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
};

Node* new_node(int data){
    Node* ptr = new Node();
    ptr->data = data;
    ptr->left = ptr->right = NULL;
    return ptr;
}

Node* insert(Node* root,int data){
    if(root == NULL) root = new_node(data);
    else if(data <= root->data) root->left = insert(root->left,data);
    else root->right = insert(root->right,data);

    return root;
}

bool search(Node* root,int data){
    if(root==NULL)return false;
    else if(root->data == data)return true;
    else if(data < root->data)return(search(root->left,data));
    else return(search(root->right,data));
}

int main(){
    Node* root;
    root = NULL;
    root = insert(root,15);
    root = insert(root,10); 
    root = insert(root,20);
    root = insert(root,25);
    root = insert(root,12);
    root = insert(root,8);
    cout<<"Enter the number to be found"<<'\n';
    int n;
    cin>>n;
    if(search(root,n)) cout<<"Found"<<'\n';
    else cout<<"Not found";
    return 0;
}
