/*
Author: Adrian Irwin
Date: 24/10/2021
This program finds the sum of all the diagonal numbers in the matrix.
*/
#include <stdio.h>
#include <stdlib.h>

/*
Function:       matrixSum
Parameters:     dimensions of the array, the array itself, the first number to add the other numbers to it
returns:        int
description:    Sums together all numbers in the diagonal of the array.
*/
int matrixSum(int dimension, int multiArray[dimension][dimension], int firstNum){
    // due to the program not working how I intended I had to make the sum start at the first number instead of 0 because the for loop wouldn't find the first number.
    int sum = firstNum;
    for (int k = 0; k < dimension; k++) // iterate through the matrix
    {
        for (int l = 0; l < dimension; l++)
        {
            if (k = l) // if we find that both the vertical and horizontal of the matrix are the same we know that it is in the diagonal so we add it to sum
            {
                sum += multiArray[k][l];
            }
        }
    }
    return sum;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Creates the matrix then calls on matrixSum to get the sum of the diagonals in the matrix.
*/
int main(int argc, char*argv[]){
    int dimension = atoi(argv[1]);
    int matrix[dimension][dimension];
    int *pMatrix = *matrix;
    int matrixSize = dimension * dimension;

    for (int i = 0; i < matrixSize; i++)
    {
        pMatrix[i] = atoi(argv[i+2]);
    }

    int firstNum = atoi(argv[2]);
    printf("%d\n", matrixSum(dimension, matrix, firstNum));

    return 0;
}