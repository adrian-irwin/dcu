/*
Author: Adrian Irwin
Date: 15/10/2021
This program checks if a number is a triangular number or not.
*/

#include <stdio.h>
#include <stdlib.h>

/*  triangular numbers 1,3,6,10,15,21,28,45...
    1 = 1, 3 = 1 + 2, 6 = 1 + 2 + 3, 10 = 1 + 2 + 3 + 4 ...
    num = number we are checking, sum = sum of all preivous and current i
*/

/*
Function:       isTriangular
Parameters:     number
returns:        int
description:    Iterate over i and add it to the sum until the we either reach i or the num,
                if we reach i and the sum is greater than the num then we know it is not a triangular number
                if sum is equal to num we know it is a triangular number
*/
int isTriangular(int num){
    int sum = 0;
    int result;
    for (int i = 0; i < num + 1; i++) // iterating over i and checking to see if num == sum
    {
        sum += i; // add i to sum

        if (sum == num)
        {
            result = 1;
            break; // break out of the loop if sum == num
        }
    }

    if (sum > num) // if the sum is greater than the num after the loop then it isnt a triangular number
    {
        result = 0;
    }
    return result;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Reads the input then calls on isTriangular using num then prints out if it is triangular or not.
*/
int main(int argc, char*argv[]){
    int num = atoi(argv[1]);
    int check = isTriangular(num);
    // result from isTriangular is used to check if the number is triangular or not
    if (check == 1)
    {
        printf("%d is a triangular number\n", num);
    }
    else if (check == 0)
    {
        printf("%d is not a triangular number\n", num);
    }

    return 0;
}