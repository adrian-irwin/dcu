#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct Node Node;

struct Node{
    int value;
    Node *next;
    Node *prev;
};

Node* findNums(char *numbers[], int size){
    Node *current, *first = (Node*)calloc(1, sizeof(Node)), *prev = NULL;

    current = first;
    current->prev = NULL;
    if (strcmp(numbers[1], "1") == 0 || strcmp(numbers[1], "0") == 0){
        current->value = atoi(numbers[1]);
    }
    else{
        current->value = 2;
    }

    for (int i = 1; i < size; i++){
        current->next = (Node*)calloc(1, sizeof(Node));
        prev = current;
        current = current->next;
        if (strcmp(numbers[i + 1], "1") == 0 || strcmp(numbers[i + 1], "0") == 0){
            current->value = atoi(numbers[i+1]);
        }
        else{
            current->value = 2;
        }
        current->prev = prev;
    }
    current->next = NULL;

    return current;
}

void binToDec (char *inputs[], int length,  int *numOutput, int *checker){
    Node *list = NULL;
    list = findNums(inputs, length);
    int count = 0;
    for (list; list != NULL; list = list->prev){
        if (list->value == 1){
            *numOutput = *numOutput + pow(2, count);
        }
        else if (list->value != 1 && list->value != 0){
            *checker = -1;
            return;
        }

        count++;
    }
}

int main(int argc, char*argv[]){
    int length = argc - 1;
    if (length > 8){
        printf("Too many binary digits entered.\n");
    }
    else{
        int numOut = 0, checker = 0;
        binToDec(argv, length, &numOut, &checker);
        if (checker == 0){
            printf("%d\n", numOut);
        }
        else{
            printf("Only digits 1 and 0 are permitted.\n");
        }
    }

    return 0;
}