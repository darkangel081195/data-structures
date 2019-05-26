#include<iostream>
#include<queue>
using namespace std;

//Binary search Tree
struct Node{
    int data;
    Node* left;
    Node* right;
};

//Creating a new node
Node* new_node(int data){
    Node* ptr = new Node();
    ptr->data = data;
    ptr->left = ptr->right = NULL;
    return ptr;
}

Node* find_min(Node* root){
    if(root->left == NULL)return root;
    else return(find_min(root->left));
}

//Inserting new node
Node* insert(Node* root,int data){
    if(root==NULL) root = new_node(data);
    else if(data <= root->data) root->left = insert(root->left,data);
    else root->right = insert(root->right,data);
    return root;
}

//Searching a node in tree
bool search(Node* root,int data){
    if(root==NULL)return false;
    else if(root->data == data)return true;
    else if(data < root->data)return(search(root->left,data));
    else return(search(root->right,data));
}

//Deleting a node
Node* delete_node(Node* root,int data){
    if(root == NULL) return root;
    else if(data < root->data) root->left = delete_node(root->left,data);
    else if(data > root->data) root->right = delete_node(root->right,data);
    else{
        //Case1: No children
        if(root->left == NULL && root->right == NULL){
            delete root;
            root = NULL;
        }
        //Case2:One child
        else if(root->right == NULL ){
            Node* temp = root;
            root = root->left;
            delete temp;
        }
        else if(root->left == NULL ){
            Node* temp = root;
            root = root->right;
            delete temp;
        }
        //Case3: Two children
        else{
            Node * temp = find_min(root->right);
            root->data = temp->data;
            root->right = delete_node(root->right,temp->data);
        }
    }
    return root;
}

//Breadth first traversal of the tree
void bfs(Node* root){
    if(root == NULL)return;
    queue<Node*> Q;
    Q.push(root);
    while(!Q.empty()){
        Node* current = Q.front();
        cout<<current->data<<' ';
        if(current->left != NULL)Q.push(current->left);
        if(current->right != NULL)Q.push(current->right);
        Q.pop();
        }
}

//Printing contents of tree in Depth first traversal
//For Preorder and post order traversal change the order to DLR and LRD respectively
void inorder(Node* root){
    if(root==NULL)return;

    inorder(root->left);//L
    cout<<root->data<<' ';//D
    inorder(root->right);//R
}

int main(){
    Node* root;
    root = NULL;
    root = insert(root,15);
    root = insert(root,10);
    root = insert(root,20);
    root = insert(root,25);
    root = insert(root,8);
    root = insert(root,12);
    inorder(root);
    cout<<'\n';
    bfs(root);
    cout<<"Enter the number to be found"<<'\n';
    int n;
    cin>>n;
    if(search(root,n)){
        cout<<"Found"<<'\n';
    }
    else{
        cout<<"Not found"<<'\n';
    }
    cout<<"Enter the number to be deleted"<<'\n';
    cin>>n;
    root = delete_node(root,n);
    cout<<"Enter the number to be found"<<'\n';
    cin>>n;
    if(search(root,n)){
        cout<<"Found"<<'\n';
    }
    else{
        cout<<"Not found"<<'\n';
    }

    return 0;
}
