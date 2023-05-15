/*
Author: Adrian Irwin
Date: 15/10/2021
This program prints all leap years in between 2 given years.
*/
#include <stdio.h>
#include <stdlib.h>

/*
Function:       leapYear
Parameters:     year1, year2, i
returns:        int
description:    Checks if the year given is a leap year.
*/
int leapYear(int yearToCheck){
    int out;
    if (((yearToCheck) % 4 == 0 && (yearToCheck) % 100 != 0) || (yearToCheck) % 400 == 0) // check if year is a leap year by checking if it can divided by 4 and (100 or 400)
    {
        out = yearToCheck;
    }
    else
    {
        out = -1; // if the year is not a leap year
    }

    return out;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Reads the input then finds all the leap years in between the given years.
*/
int main(int argc, char*argv[]){
    int year1 = atoi(argv[1]), year2 = atoi(argv[2]); // assign first and second args to the start and end years

    for (int i = 0; i <= year2 - year1 ; i++) // cycle through all years from year1 to year2
    {
        int yearToCheck = year1 + i; // set the year to check
        int leap = leapYear(yearToCheck); // pass the year through the leapYear function
        if (leap != -1)
        {
            printf("%d\n", leap);
        }
    }

    return 0;
}