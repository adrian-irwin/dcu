/*
Author: Adrian Irwin
Date: 25/10/2021
This program multiplies two matrices together.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// example input = ./lab5-multiple-matrix 3 3 1 2 3 6 5 4 8 7 9 3 2 1 2 9 8 6 7
// first two args are dims for matrix 1


/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Takes in command line arguments and turns them into the respective matrices, the two matrices are then multiplied by each other and printed out.
*/
int main(int argc, char*argv[]){
    // stuff to make matrix one
    int matrixOneRow = atoi(argv[1]);
    int matrixOneColumn = atoi(argv[2]);
    int matrixOne[matrixOneRow][matrixOneColumn];
    int *pMatrixOne = *matrixOne;
    int matrixOneSize = matrixOneRow * matrixOneColumn;

    // add stuff to matrix one
    for (int i = 0; i < matrixOneSize; i++)
    {
        pMatrixOne[i] = atoi(argv[i+3]);
    }

    // stuff to make matrix two
    int matrixTwoRow = atoi(argv[3+matrixOneSize]);
    int matrixTwoColumn = atoi(argv[4+matrixOneSize]);
    int matrixTwo[matrixTwoRow][matrixTwoColumn];
    int *pMatrixTwo = *matrixTwo;
    int matrixTwoSize = matrixTwoRow * matrixTwoColumn;

    //add stuff to matrix two
    for (int i = 0; i < matrixTwoSize; i++)
    {
        pMatrixTwo[i] = atoi(argv[i+5+matrixOneSize]);
    }

    // initialise final matrix
    int finalMatrix[matrixOneRow][matrixTwoColumn];
    // multiply matrices
    for (int row = 0; row < matrixOneRow; row++){ // for every row in the matrix
        for (int column = 0; column < matrixTwoColumn; column++){ // for every column in the matrix
            finalMatrix[row][column] = 0; // set the value for each to 0 so the sum starts off at 0
            for (int i = 0; i < matrixTwoRow; i++){
                finalMatrix[row][column] += matrixOne[row][i] * matrixTwo[i][column]; // add the multiplication of the numbers from both matrix1 and martix2
            }
        }
    }
    // print out the values in the matrix after multiplying it
    for (int row = 0; row < matrixOneRow; row++)
    {
        for (int column = 0; column < matrixTwoColumn; column++)
        {
            if (column != matrixTwoColumn - 1) // if we are not printing the last one we print it with a space
            {
                printf("%d ", finalMatrix[row][column]);
            }
            else // we print without a space if we are not printing the last value in the column.
            {
                printf("%d", finalMatrix[row][column]);
            }
        }
        printf("\n");
    }

    return 0;
}