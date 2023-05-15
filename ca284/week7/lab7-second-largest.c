/*
Author: Adrian Irwin
Date: 04/11/2021
This program takes a list of numbers and finds the second largest number in the list.
*/

// input == list of float nums.
// find second largest number in the list

#include <stdio.h>
#include <stdlib.h>

/*
Function:       makeList
Parameters:     size of the list, numbers to be put into the list, pointer to the list
returns:        void
description:    Makes a list that contains the given numbers.
*/
void makeList(int size, char *numbers[], float *list){
    for (int i = 0; i < size; i++){
        *(list + i) = atof(numbers[i+1]);
    }
}

/*
Function:       maxTwo
Parameters:     pointer to the list, size of the list
returns:        float
description:    Finds the second largest number in the list.
*/
float maxTwo(float *list, int size){
    // assign both max and secondMax to the start of the list
    float max = *list;
    float secondMax = *list;

    for (int i = 0; i < size; i++){
        if (*(list + i) > max){ // if the number we are checking is greater than the current max we assign secondMax to the previous max and assign the current number to max
            secondMax = max;
            max = *(list + i);
        }
        else if (*(list + i) < max && *(list + i) > secondMax){ // if the number we are checking is greater than the secondMax but is less than max we assign it to secondMax
            secondMax = *(list + i);
        }
    }
    return secondMax;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    initalize a list using malloc then add the given numbers to the list by calling makeList, lastly we print the second largest number by calling maxTwo
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    // use malloc to create the list for the numbers with enough memory for all the numbers
    float *numbers = malloc(length * sizeof(float));
    if (!numbers){ // if we cant make the list we stop the program and free the memory
        printf("Not enough memory!\n");
        free(numbers);
        numbers = NULL;
        exit(0);
    }

    makeList(length, argv, numbers);
    printf("%.1f\n", maxTwo(numbers, length));
    // before the program ends we free the memory that we used to make the list
    free(numbers);
    numbers = NULL;
    return 0;
}