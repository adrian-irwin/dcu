#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

// create the struct that is used in the linked list to store values and the node before and after the current value
struct Node{
    float value;
    Node *next;
    Node *prev;
};


// get numbers from command line input and put it into a linked list
Node* findNums(char *numbers[], int size){
    // create three nodes, first is the start point of the linked list, current is the current node we are putting values into and prev is the a temporary node to store the previous node
    Node *current, *first = (Node*)calloc(1, sizeof(Node)), *prev = NULL;
    current = first; // assign current to first so we start at first
    current->prev = NULL; // make sure that there is no value before the first node
    current->value = atof(numbers[2]); // give the first value into the first node
    for (int i = 1; i < size; i++){
        current->next = (Node*)calloc(1, sizeof(Node)); // create a node after our current one to store another value
        prev = current; // store our current value to reassing it as the previous node of the next node
        current = current->next; // move to the next node
        current->value = atof(numbers[i+2]); // assign the number to the value of the current node
        current->prev = prev; // assign the last node to the prev node of current
    }
    current->next = NULL; // make sure that there is no node after our final value

    return current; // return a pointer to the end position of the linked list
}

void printLinkedListReverse(Node *start){
    for (start; start != NULL; start = start->prev){
        printf("%.2f\n", start->value);
    }
}


int main(int argc, char*argv[]){
    int length = atoi(argv[1]);
    Node *lList = NULL;
    lList = findNums(argv, length);
    printLinkedListReverse(lList);
    return 0;
}
