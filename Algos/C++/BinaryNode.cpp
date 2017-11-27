#include <iostream>

class BinaryNode{
public:
    int key;
    BinaryNode * left;
    BinaryNode * right;
    BinaryNode();
    int getSize();
}

BinaryNode::BinaryNode(int key){
    this->key = key;
}

int BinaryNode::getSize(){
    if (!left && !right){
        return 1;
    }
    else{
        return 1 + this->left->getSize() + this->right->getSize();
    }
}

int main(){
    BinaryNode b = BinaryNode(5);
    BinaryNode l = BinaryNode(3);
    BinaryNode r = BinaryNode(8);

    b->left = l;
    b->right = r;
    int n = b.getSize();
    printf("%d\n", n);
}
