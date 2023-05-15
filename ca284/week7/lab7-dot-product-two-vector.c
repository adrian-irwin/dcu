/*
Author: Adrian Irwin
Date: 04/11/2021
This program takes two vectors and finds the dot product of them.
*/

// find dot product of two vectors, size n, n = first argument
// example input: ./lab7-dot-product-two-vector 3 1 2 3 4 -5 6
// two vectors of size 3, vector1 = (1,2,3), vector2 = (4,-5,6)
// (1*4)+(2*-5)+(3*6)
// answer: 12

#include <stdio.h>
#include <stdlib.h>

/*
Function:       makeVectors
Parameters:     size of the vectors, numbers to be put into the vectors, pointer to the first vector, pointer to the second vector
returns:        void
description:    Makes 2 vectors using the given list of numbers.
*/
void makeVectors(int size, char *numbers[], int *firstVector, int *secondVector){
    for (int i = 0; i < size; i++)
    {
        *(firstVector+i) = atoi(numbers[i+2]);
        *(secondVector+i) = atoi(numbers[i+size+2]);
    }
}

/*
Function:       dotProduct
Parameters:     pointer to the first vector, pointer to the second vector, size of the two vectors
returns:        int
description:    Finds the dot prodcut of the two vectors.
*/
int dotProduct (int *firstVector, int *secondVector, int size){
    int product = 0;
    for (int i = 0; i < size; i++)
    {
        // to find the dot product we multiply two numbers at the same position in both vectors and then add it to the overall product, this is done until we reach the end of both vectors.
        product += *(firstVector+i) * *(secondVector+i);
    }

    return product;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    initalize two vectors using calloc, we then add numbers to the vectors by calling makeVectors, we then print the dot product by calling dotProduct
*/
int main(int argc, char*argv[]){
    int vectorSize = atoi(argv[1]);
    // use calloc to create two vectors the length of the numbers
    int *vector1 = calloc(vectorSize, sizeof(int));
    int *vector2 = calloc(vectorSize, sizeof(int));
    if (!vector1 && !vector2) // if we cant make the vectors we stop the program and free the memory
    {
        printf("Not enough memory!\n");
        free(vector1);
        free(vector2);
        vector1 = NULL, vector2 = NULL;
        exit(0);
    }

    makeVectors(vectorSize, argv, vector1, vector2);

    printf("%d\n", dotProduct(vector1, vector2, vectorSize));

    // before the program ends we free the memory that we used to make the vectors
    free(vector1);
    free(vector2);
    vector1 = NULL, vector2 = NULL;
    return 0;
}