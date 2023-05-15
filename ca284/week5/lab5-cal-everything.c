/*
Author: Adrian Irwin
Date: 25/10/2021
This program gives multiple calculations for 2 given integers.
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// To make the code cleaner all the calculation functions are done on one line each
double sum(float a, float b){return a + b;}
double difference(float a, float b){return a - b;}
double product(float a, float b){return a * b;}
double division(float a, float b){return a / b;}
double power(float a, float b){return pow(a, b);}
double naturalLog(float a, float b){return log(a) + log(b);}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Stores the integers given then calls on each of the calculation functions.
*/
int main(int argc, char*argv[]){
    float a = atof(argv[1]);
    float b = atof(argv[2]);
    double result = 0;
    double (*pFunction)(float, float);

    pFunction = sum;
    result = pFunction(a,b);
    printf("%.2f\n", result);

    pFunction = difference;
    result = pFunction(a,b);
    printf("%.2f\n", result);

    pFunction = product;
    result = pFunction(a,b);
    printf("%.2f\n", result);

    pFunction = division;
    result = pFunction(a,b);
    printf("%.2f\n", result);

    pFunction = power;
    result = pFunction(a,b);
    printf("%.2f\n", result);

    pFunction = naturalLog;
    result = pFunction(a,b);
    printf("%.2f\n", result);
    return 0;
}