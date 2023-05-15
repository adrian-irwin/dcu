/*
Program: ex4-order-linked-list.c
Author: Adrian Irwin
Date: 10/12/2021
This program accepts n float numbers and makes a doubly linked list to store the numbers.
The program then checks if the list is in descending order and prints 1 if it is, otherwise it prints 0.
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node{
    float value;
    Node *next;
    Node *prev;
};

// function prototypes
Node* findNums(char *numbers[], int size);
int checkOrder(Node *number);

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Create a doubly linked list and add numbers to it using findNums.
                prints if the list is in order or not using checkOrder
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    Node *lList = NULL;
    lList = findNums(argv, length);
    printf("%d\n", checkOrder(lList));
    return 0;
}

/*
Function:       findNums
Parameters:     numbers to add to the list, size of the numbers.
returns:        Node*
description:    Return a pointer to the list after adding the numbers.
*/
Node* findNums(char *numbers[], int size){
    Node *current, *first = (Node*)calloc(1, sizeof(Node)), *prev = NULL;
    if (!first){
        printf("Not enough memory!\n");
        exit(0);
    }
    current = first;
    current->prev = NULL;
    current->value = atof(numbers[1]);
    for (int i = 1; i < size; i++){
        current->next = (Node*)calloc(1, sizeof(Node));
        if (!current->next){
            printf("Not enough memory!\n");
            exit(0);
        }
        prev = current;
        current = current->next;
        current->value = atof(numbers[i+1]);
        current->prev = prev;
    }
    current->next = NULL;
    return first;
}

/*
Function:       checkOrder
Parameters:     numbers to add to the list, size of the numbers.
returns:        int
description:    Returns 1 if the list is in descending order and 0 if it is not.
*/
int checkOrder(Node *number){
    int check = 1;
    number = number->next;
    for (; number != NULL; number = number->next){
        if (number->value > number->prev->value){
            check = 0;
        }
    }
    return check;
}
