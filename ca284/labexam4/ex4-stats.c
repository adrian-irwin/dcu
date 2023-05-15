/*
Program: ex4-stats.c
Author: Adrian Irwin
Date: 10/12/2021
This program accepts a number of integers with the last integer being what we want to do with our integer.
If the last integer is 1 we output the max value.
If the last integer is 2 we output the most frequent integer.
If the last integer is 3 we output the standard deviation of the integers.
If the last integer is none of these we just output the max value.
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// function prototypes
void addNumbers(int *finalList, char *numsToAdd[], int size);
float max(int *nums, int size);
float mode(int *nums, int size);
float standardDeviation(int *nums, int size);
void printResult(int* nums, int size, int operation);

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Makes an array using memory allocation to store numbers.
                Call addNumbers to add numbers to the array.
                Call printResult to the result based on the last integer in the array.
*/
int main(int argc, char*argv[]){
    int length = argc - 2;
    int last = atoi(argv[argc - 1]);

    int *numbers = (int*)calloc(length, sizeof(int));
    if (!numbers){
        printf("Not enough memory!\n");
        exit(0);
    }

    addNumbers(numbers, argv, length);
    printResult(numbers, length, last);

    return 0;
}

/*
Function:       addNumbers
Parameters:     list to add numbers to, numbers to be added to the list, size of the list
returns:        void
description:    Adds numbers into the list.
*/
void addNumbers(int *finalList, char *numsToAdd[], int size){
    for (int i = 0; i < size; i++){
        *(finalList + i) = atoi(numsToAdd[i + 1]);
    }

}

/*
Function:       max
Parameters:     list of numbers, size of the list
returns:        float
description:    Finds the biggest number in the list.
*/
float max(int *nums, int size){
    int max = 0;
    for (int i = 1; i < size; i++){
        if (*(nums + i) > *(nums + i - 1)){
            max = *(nums + i);
        }
    }
    return max;
}

/*
Function:       mode
Parameters:     list of numbers, size of the list
returns:        float
description:    Finds the most frequent number in the list.
*/
float mode(int *nums, int size){
    int mode = 0, highestCount = 0, count = 0;
    for (int i = 0; i < size; i++){
        count = 0;
        for (int j = 0; j < size; j++){
            if (*(nums +j) == *(nums + i)){
                count++;
            }
        }
        if (count > highestCount){
            highestCount = count;
            mode = *(nums + i);
        }
    }
    return mode;
}

/*
Function:       standardDeviation
Parameters:     list of numbers, size of the list
returns:        float
description:    Finds the standard deviation of all the numbers in the list.
*/
float standardDeviation(int *nums, int size){
    int sum = 0;
    float sd = 0.0, mean = 0.0;
    for (int i = 0; i < size; i++){
        sum += *(nums + i);
    }
    mean = sum / size;
    for (int i = 0; i < size; i++){
        sd += pow(*(nums + i) - mean, 2);
    }
    return sqrt(sd / size);
}

/*
Function:       printResult
Parameters:     list of numbers, size of the list, operation to execute
returns:        void
description:    Print the result of a given operation on a given list of numbers.
*/
void printResult(int* numbers, int size, int operation){
    float result = 0.0;
    float (*pFunction)(int*, int);
    switch (operation){
    case 1:
        pFunction = max;
        result = pFunction(numbers, size);
        printf("%.0f\n", result);
        break;

    case 2:
        pFunction = mode;
        result = pFunction(numbers, size);
        printf("%.0f\n", result);
        break;

    case 3:
        pFunction = standardDeviation;
        result = pFunction(numbers, size);
        printf("%.2f\n", result);
        break;

    default:
        pFunction = max;
        result = pFunction(numbers, size);
        printf("%.0f\n", result);
        break;
    }
}