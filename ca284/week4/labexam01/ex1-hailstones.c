/*
Author: Adrian Irwin
Date: 15/10/2021
This program prints the numbers in the hailstone sequence up until it reaches 1.
*/

#include <stdio.h>
#include <stdlib.h>

/*
Function:       hailstone
Parameters:     number
returns:        int
description:    Gets hailstone sequence from number.
*/
int hailstone(int number){
    if (number % 2 == 0) // if even divide by 2
    {
        number = number / 2;
    }
    else if (number % 2 == 1) // if odd multiply by 3 and add 1
    {
        number = (number * 3) + 1;
    }
    return number;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Reads the input then calls on the hailstone function to find the hailstone sequence of the number.
*/
int main(int argc, char*argv[]){
    int n = atoi(argv[1]);
    printf("%d", n);

    do // do while loop to get the hailstone sequence until we get to n = 1
    {
        n = hailstone(n);
        printf(" %d", n);
    } while (n != 1);

    printf("\n");

    return 0;
}