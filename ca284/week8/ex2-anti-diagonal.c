/*
Program: ex2-anti-diagonal.c
Author: Adrian Irwin
Date: 11/11/2021
This program takes a given square matrix of given n size and prints out the sum of the anti-diagonal elements in the matrix.
*/
#include <stdio.h>
#include <stdlib.h>

/*
Function:       makeMatrix
Parameters:     pointer to matrix, size of matrix, pointer to numbers to put into matrix
returns:        void
description:    Adds numbers to given matrix.
*/
void makeMatrix(int *matrix, int size, char *numbers[]){
    for (int i = 0; i < size; i++){
        *(matrix + i) = atoi(numbers[i + 2]);
    }
}

/*
Function:       sumMatrix
Parameters:     dimension of given matrix, matrix to take numbers from to add together.
returns:        int
description:    Adds up anti-diagonal elements of matrix together
*/
int sumMatrix(int dimension, int *matrixOne){
    int sum = 0;
    for (int i = 0; i < dimension; i++){ // on every row of the matrix we go loop through the columns backwards row by row so that we can easily add them together.
        int x = dimension * i;
        int y = dimension - i - 1;
        sum += *(matrixOne + x + y);
    }
    return sum;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Makes a matrix using the makeMatrix function then prints out the sum of the anti-diagonal elements in the matrix by calling sumMatrix.
*/
int main(int argc, char*argv[]){
    int dims = atoi(argv[1]);
    int matrixSize = dims * dims;
    int matrix[dims][dims];

    makeMatrix(*matrix, matrixSize, argv);
    printf("%d\n", sumMatrix(dims, *matrix));

    return 0;
}