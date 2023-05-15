/* Include standard input and output */
#include <stdio.h>
#include <stdlib.h>
/*
Function: Main
Parameters: none
returns: int
description: Get 2 input interger from command-line, add them up and print out the result
*/

int main(int argc, char*argv[])

{

   int number1, number2, sum;

   number1 = atoi(argv[1]);
   number2 = atoi(argv[2]);
   sum = number1 + number2;

   printf("The sum result is: %d\n", sum);

   return 0;
}