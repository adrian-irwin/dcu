/*
Program: ex2-degree-array.c
Author: Adrian Irwin
Date: 11/11/2021
This program finds the degree of a given array.
The degree of an array is the number of times the most frequent element in an array is in given array.
*/
#include <stdio.h>
#include <stdlib.h>

/*
Function:       makeArray
Parameters:     size of the array, numbers to be put into the array, pointer to the array
returns:        void
description:    Makes an array that contains the given numbers.
*/
void makeArray(int size, char *numbers[], int *list){
    for (int i = 0; i < size; i++){
        *(list + i) = atoi(numbers[i+1]);
    }
}

/*
Function:       mostCommon
Parameters:     pointer to the array, length of the array
returns:        int
description:    Returns the count of the most common element in an array.
*/
int mostCommon(int *list, int length){
    int count = 0;
    int max = 0;
    for (int i = 0; i < length; i++){
        for (int j = 0; j < length; j++){
            if (*(list + i) == *(list + j)){
                count++;
            }
        }
        if (count > max){
            max = count;
        }
        count = 0;
    }

    return max;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Make an array using the makeArray function, prints and finds the degree of the array using the mostCommon function.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    int numbers[length];
    makeArray(length, argv, numbers);
    printf("%d\n", mostCommon(numbers, length));
    return 0;
}