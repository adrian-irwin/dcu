#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

// create the struct that is used in the linked list to store values and the node after the current value
struct Node{
    int value;
    Node *next;
};

// get numbers from command line input and put it into a linked list
Node* findNums(char *numbers[], int size){
    // create two nodes, first is the start point of the linked list and current is the current node we are putting values into
    Node *current, *first = (Node*)calloc(1, sizeof(Node));
    current = first; // assign current to first so we start at first
    current->value = atoi(numbers[2]); // give the first value into the first node
    for (int i = 1; i < size; i++)
    {
        current->next = (Node*)calloc(1, sizeof(Node)); // create a node after our current one to store another value
        current = current->next; // move to the next node
        current->value = atoi(numbers[i+2]); // assign the number to the value of the current node
    }
    current->next = NULL; // make sure that there is no node after our final value

    return first; // return a pointer to the start position of the linked list
}

void printLinkedList(Node *start){
    for (start; start != NULL; start = start->next){
        printf("%d\n", start->value);
    }
}


int main(int argc, char*argv[]){
    int length = atoi(argv[1]);
    Node *lList = NULL;
    lList = findNums(argv, length);
    printLinkedList(lList);
    return 0;
}
