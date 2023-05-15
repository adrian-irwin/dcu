/*
Program: ex2-median.c
Author: Adrian Irwin
Date: 11/11/2021
This program finds the two center numbers in a sorted list that has even elements.
*/
#include <stdio.h>
#include <stdlib.h>

/*
Function:       bubSort
Parameters:     pointer to the list we want to sort, size of the list
returns:        void
description:    sorts the list in ascending order using bubble sort.
                Bubble sort sort by looping through the elements and if the next element is smaller than the current one we swap them
*/
void bubSort(int *list, int length){
    for (int i = 0; i < length - 1; i++){
        for (int j = 0; j < length - i - 1; j++){
            if (*(list + j) > *(list + j + 1)){
                int temp = *(list + j);
                *(list + j) = *(list + j + 1);
                *(list + j + 1) = temp;
            }
        }
    }
}

/*
Function:       makeArray
Parameters:     size of the list, numbers to be put into the list, pointer to the list
returns:        void
description:    Makes a list that contains the given numbers.
*/
void makeArray(int size, char *numbers[], int *list){
    for (int i = 0; i < size; i++){
        *(list + i) = atoi(numbers[i+1]);
    }
}


/*
Function:       medianNumbers
Parameters:     pointer for where to store the first median, pointer for where to store the second median, the list of numbers, size of the list
returns:        void
description:    Finds the median numbers and assigns it to two variables which are accessed with pointers.
*/
void medianNumbers(int *x, int *y, int *list, int *size){
    *x = list[*size / 2 - 1];
    *y = list[*size / 2];
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Make an array using the makeArray function, the array then gets sorted. Call medianNumbers to find the two numbers at the median and print the two median numbers.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    int numbers[length];
    makeArray(length, argv, numbers);

    bubSort(numbers, argc - 1);

    int medianOne, medianTwo;
    medianNumbers(&medianOne, &medianTwo, numbers, &length);
    printf("%d\n%d\n", medianOne, medianTwo);

    return 0;
}