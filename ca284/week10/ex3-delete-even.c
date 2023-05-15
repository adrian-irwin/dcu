/*
Program: ex3-delete-even.c
Author: Adrian Irwin
Date: 25/11/2021
This program creates a list of positive integers from the command line.
All even numbers are found and deleted from the list.
The program the calculates the sum of the remaining odd numbers and pushes the result to the list.
Finally, the numbers are printed line by line.
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node{
    int value;
    Node *next;
    Node *prev;
};

// we need functions to find the numbers, remove the even numbers from the list, find the sum of the remaining odd numbers and print the list.
Node* findNums(char *numbers[], int size);
Node* removeEven(Node* list);
Node* sum (Node* list);
void printLinkedList(Node *start);


/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    makes an array of numbers using the command line arguments by calling findNums,
                remove the even numbers from the list using removeEven,
                find the sum of the remaining odd numbers and push it to the list using sum and print the list using printLinkedList.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    Node *lList = findNums(argv, length), *temp = NULL;
    lList = removeEven(lList);

    lList = sum(lList);
    printLinkedList(lList);

    return 0;
}

/*
Function:       findNums
Parameters:     numbers to be put into the list, size of the list
returns:        Node*
description:    Makes a list that contains the given numbers and returns a pointer to the start of the list.
*/
Node* findNums(char *numbers[], int size){
    Node *current, *first = (Node*)calloc(1, sizeof(Node)), *prev = NULL;
    current = first;
    current->prev = NULL;
    current->value = 1;
    for (int i = 0; i < size; i++){
        current->next = (Node*)calloc(1, sizeof(Node));
        prev = current;
        current = current->next;
        current->value = atoi(numbers[i+1]);
        current->prev = prev;
    }
    current->next = NULL;

    return first;
}

/*
Function:       removeEven
Parameters:     pointer to a list of numbers
returns:        Node*
description:    Removes even numbers from the given list of numbers.
*/
Node* removeEven(Node* list){
    Node *p, *first = NULL, *temp = NULL;
    first = list;
    p = first;
    for (p->next; p != NULL; p = p->next){
        if (p->value % 2 == 0){
            if (p->prev != NULL && p->next != NULL){
                p->prev->next = p->next;
                p->next->prev = p->prev;
                temp = p->prev;
                free(p);
                p = temp;
            }
            else if (p->next == NULL)
            {
                p = p->prev;
                p->next = NULL;
            }
        }
    }
    return first;
}


/*
Function:       printLinkedList
Parameters:     pointer to the start a list of numbers
returns:        void
description:    Prints the elements from the given list.
*/
void printLinkedList(Node *start){
    for (start = start->next; start != NULL; start = start->next){
        printf("%d\n", start->value);
    }
}

/*
Function:       sum
Parameters:     pointer to a list of numbers
returns:        Node*
description:    Adds together the elements of the given list and adds the sum to the list.
*/
Node* sum(Node* list){
    int total = 0;
    Node *p;
    p = list;
    for (p = p->next; p != NULL; p = p->next){
        total += p->value;
    }


    Node *first = NULL, *temp = NULL, *prev = NULL;
    p = NULL;
    first = list;
    p = first;
    for (p->next; p != NULL; p = p->next){
        if (p->next == NULL){
            p->next = (Node*)calloc(1, sizeof(Node));
            prev = p;
            p = p->next;
            p->prev = prev;
            p->value = total;
        }
    }
    return first;
}