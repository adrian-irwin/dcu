#include <stdio.h>
/*
Function: Main
Parameters: none
returns: int
description: Declare and print out some variables with different types
*/

int main(int argc, char*argv[]){
    int age = 19;
    long studentId = 999999999;
    float height = 1.8f;
    char initial = 'P';
    char first_name[] = "Adrian";
    char last_name[] = "Irwin";

    printf("I have a first name %s.\n", first_name);
    printf("I have a last name %s.\n", last_name);
    printf("I have an initial %c.\n", initial);
    printf("My whole name is %s %c. %s.\n", first_name, initial, last_name);
    printf("I am %d years old.\n", age);
    printf("I am %f m tall.\n", height);
    printf("My student ID is %ld.\n", studentId);

    float monthlySalary;
    double annualSalary;

    monthlySalary = 1234.56;
    annualSalary = monthlySalary*12;

    printf("My monthly salary is %f euros.\n", monthlySalary);
    printf("My annual gross salary is %f euros.\n", annualSalary);

    return(0);
}
