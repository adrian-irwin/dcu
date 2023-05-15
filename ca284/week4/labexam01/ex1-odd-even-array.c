/*
Author: Adrian Irwin
Date: 15/10/2021
This program adds the odd elements of an array together and subtracts the even elements from each other.
*/
#include <stdio.h>
#include <stdlib.h>

/*
Function:       oddNums
Parameters:     list of numbers, length of the list of numbers
returns:        int
description:    Finds all odd numbers and adds each odd number to each other.
*/
int oddNums (int numbers[], int length){
    int sum = 0;
    for (int i = 0; i < length; i++) // reads all of the input and add the odd numbers to sum
    {
        if (numbers[i] % 2 == 1)
        {
            sum += numbers[i];
        }
    }
    return sum;
}

/*
Function:       evenNums
Parameters:     list of numbers, length of the list of numbers
returns:        int
description:    Finds the first even number and sets it as the base number to subtract from and all even numbers past the first even number will be subtracted from the base number.
*/
int evenNums (int numbers[], int length){

    int subtract = 0;
    int position = 0;

    do // do while loop to find the first even number if one exists
    {
        if (numbers[position] % 2 == 0)
        {
            subtract = numbers[position];
        }
        position++;
    } while (subtract == 0 && position < length); // stops if subtract is still 0 because we dont have an even number and if we reach the end of the string
    // position ends up as the new start point for the even numbers because we know that there are no even numbers before position
    for (position; position < length; position++) // this loop wont do anything if we dont have any even numbers and subtract stays as 0
    {
        if (numbers[position] % 2 == 0)
        {
            subtract -= numbers[position];
        }
    }
    return subtract;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    reads the input and stores it, then calls on oddNums and evenNums and prints their output
*/
int main(int argc, char*argv[]){

    int length = argc - 1;
    int list1[length];

    for (int i = 0; i < length; i++) // read and store inputs in an array
    {
        list1[i] = atoi(argv[i+1]);
    }

    // assign results of both odd and even to relevant variables
    int odd = oddNums(list1, length);
    int even = evenNums(list1, length);

    // print both odd and even
    printf("%d\n", odd);
    printf("%d\n", even);

    return 0;
}