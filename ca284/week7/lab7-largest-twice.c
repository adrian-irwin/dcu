/*
Author: Adrian Irwin
Date: 05/11/2021
This program takes a list of numbers and finds the largest number in the list that is also double another number.
*/

// input == list of integer numbers
// find the largest number that is double one number in the array
// if none can be found print 0

#include <stdio.h>
#include <stdlib.h>

/*
Function:       makeList
Parameters:     size of the list, numbers to be put into the list, pointer to the list
returns:        void
description:    Makes a list that contains the given numbers.
*/
void makeList(int size, char *numbers[], int *list){
    for (int i = 0; i < size; i++){
        *(list + i) = atof(numbers[i+1]);
    }
}

/*
Function:       sort
Parameters:     pointer to the list, size of the list
returns:        void
description:    sorts the list using bubble sort
*/
void sort(int *list, int size){
    for (int i = 0; i < size; i++){ // bubble sort is used to sort the list in ascending order
        for (int j = 0; j < size - i - 1; j++){
            if (*(list + j) > *(list + j + 1)){
                int tmp = *(list + j);
                *(list + j) = *(list + j + 1);
                *(list + j + 1) = tmp;
            }
        }
    }
}

/*
Function:       findTwiceNumber
Parameters:     pointer to the list, size of the list
returns:        int
description:    Finds the largest number that is also double another number.
*/
int findTwiceNumber(int *list, int size){
    int stored = 0; // make an integer to keep the number to be returned
    for (int k = 0; k < size; k++){
        for (int l = 0; l < size; l++){ // we go through the list until we find a number that is also double another number
            if ((float)*(list + k) / 2 == (float)*(list + l)){ // we convert the numbers into float so that we can accurately find numbers that are double another number
                stored = *(list + k);
            }
        }
    }
    return stored; // due to our list being sorted we should have the largest number that is also double another number stored in our variable.
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    initalize a list using calloc then add the given numbers to the list by calling makeList, we sort the list using the sort function.
                Lastly we print the largest number in the list that is also double another number by calling the findTwiceNumber function.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    // use calloc to create the list for the numbers with enough memory for all the numbers
    int *numbers = calloc(length, sizeof(int));
    if (!numbers){ // if we cant make the list we stop the program and free the memory
        printf("Not enough memory!\n");
        free(numbers);
        numbers = NULL;
        exit(0);
    }

    makeList(length, argv, numbers);
    sort(numbers, length);
    printf("%d\n", findTwiceNumber(numbers, length));
    
    // before the program ends we free the memory that we used to make the list
    free(numbers);
    numbers = NULL;
    return 0;
}