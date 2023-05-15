/*
Author: Adrian Irwin
Date: 15/10/2021
This program prints the largest or smallest number in a given array depending on the first input given.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Function:       smallest
Parameters:     list of numbers, length of the list of numbers
returns:        int
description:    Finds the smallest number in given list of numbers.
*/
float smallest(float numbers[], int length){
    float small = numbers[0]; // start at the first position of the list
    for (int i = 0; i < length; i++)
    {
        if (numbers[i] < small) // if numbers[i] is smaller than small make it the new smallest number
        {
            small = numbers[i];
        }

    }
    return small;
}

/*
Function:       largest
Parameters:     list of numbers, length of the list of numbers
returns:        int
description:    Finds the largest number in given list of numbers.
*/
float largest(float numbers[], int length){
    float large = numbers[0]; // start at the first position of the list
    for (int i = 0; i < length; i++)
    {
        if (numbers[i] > large) // if numbers[i] is larger than large make it the new largest number
        {
            large = numbers[i];
        }

    }
    return large;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Reads the input then calls on either smallest or largest and prints the smallest or largest number
*/
int main(int argc, char*argv[]){
    char operator[50];
    strcpy(operator, argv[1]); // copy the first argument to a variable

    int length = argc - 2;
    float numbers[length];

    for (int i = 0; i < length; i++) // add all arguments to a list without the first argument
    {
        numbers[i] = atof(argv[i+2]);
    }

    float result;
    if (strcmp(operator, "smallest") == 0) // check to see if we are finding the smallest
    {
        result = smallest(numbers, length);
    }
    else if (strcmp(operator, "largest") == 0) // check to see if we are finding the largest
    {
        result = largest(numbers, length);
    }

    printf("%.2f\n", result);

    return 0;
}