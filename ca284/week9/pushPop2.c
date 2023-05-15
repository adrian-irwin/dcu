#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

// create the struct that is used in the linked list to store values and the node before and after the current value
struct Node{
    int value;
    Node *next;
    Node *prev;
};


// get numbers from command line input and put it into a linked list
Node* findNums(char *numbers[], int size){
    // create three nodes, first is the start point of the linked list, current is the current node we are putting values into and prev is the a temporary node to store the previous node
    Node *current, *first = (Node*)calloc(1, sizeof(Node)), *prev = NULL;
    current = first; // assign current to first so we start at first
    current->prev = NULL; // make sure that there is no value before the first node
    current->value = atoi(numbers[2]); // give the first value into the first node
    for (int i = 1; i < size; i++){
        current->next = (Node*)calloc(1, sizeof(Node)); // create a node after our current one to store another value
        prev = current; // store our current value to reassing it as the previous node of the next node
        current = current->next; // move to the next node
        current->value = atoi(numbers[i+2]); // assign the number to the value of the current node
        current->prev = prev; // assign the last node to the prev node of current
    }
    current->next = NULL; // make sure that there is no node after our final value

    return current; // return a pointer to the end position of the linked list
}

Node* pushPop (Node* list, int size, int popPush, char *numbers[]){
    Node *p, *prev = NULL, *temp = NULL;
    p = list;
    //POP
    for (int i = 0; i < popPush; i++){
        if(p != NULL){
            p = p->prev;
            p->next = NULL;
        }
    }

    // printf("value before: %d\n", p->prev->value);
    // printf("stopped at: %d\n", p->value);
    // printf("asdasd: %d\n", p->next->value);

    // p->next = (Node*)calloc(1, sizeof(Node));
    // prev = p;
    // p = p->next;
    // p->prev = prev;
    // p->value = atoi("1");

    // printf("stopped at: %d\n", p->value);
    // printf("asdasd: %d\n", p->next->value);
    // printf("value before: %d\n", p->prev->value);
    // printf("value before: %d\n", p->prev->prev->value);
    // printf("value before: %d\n", p->prev->prev->prev->value);
    // printf("value before: %d\n", p->prev->prev->prev->prev->value);


    // PUSH
    for (int i = 0; i < popPush; i++){
        p->next = (Node*)calloc(1, sizeof(Node));
        prev = p;
        p = p->next;
        p->prev = prev;
        p->value = atoi(numbers[i + size + 2]);
    }
    p->next = NULL;

    for (p; p->prev != NULL;p = p->prev){}

    // printf("stopped at: %d\n", p->value);
    return p;
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
    int popPush = argc - 2 - length;
    lList = pushPop(lList, length, popPush, argv);

    printLinkedList(lList);

    return 0;
}
