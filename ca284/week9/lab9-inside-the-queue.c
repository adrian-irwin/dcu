#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

// create the struct that is used in the linked list to store values and the node before and after the current value
struct Node{
    int value;
    Node *next;
    Node *prev;
};

Node* makeLinkedList(int numbers[]){
    Node *current, *first = (Node*)calloc(1, sizeof(Node)), *prev = NULL;
    current = first; // assign current to first so we start at first
    current->prev = NULL; // make sure that there is no value before the first node
    current->value = numbers[0]; // give the first value into the first node
    for (int i = 1; i < 10; i++){
        current->next = (Node*)calloc(1, sizeof(Node));
        prev = current;
        current = current->next;
        current->value = numbers[i];
        current->prev = prev;
    }
    current->next = NULL;

    return first;
}

void placeAfter(Node *list, int find, int add){
    Node *temp = NULL;
    for(list; list != NULL; list = list->next){
        if(list->value == find){
            temp = list->next;
            list->next = (Node*)calloc(1, sizeof(Node));
            list->next->next = temp;
            list->next->value = add;
        }
    }
}

void printLinkedList(Node *start){
    for (start; start != NULL; start = start->next){
        printf("%d\n", start->value);
    }
    // printf("----------\n");
}


int main(int argc, char*argv[]){
    int numToFind = atoi(argv[1]);
    int addAfter = atoi(argv[2]);
    int numbers[10] = {8, 7, 3, 4, 5, 6, 9, 2, 14, 12};

    Node *lList = NULL;
    lList = makeLinkedList(numbers);
    placeAfter(lList, numToFind, addAfter);
    printLinkedList(lList);
    return 0;
}
