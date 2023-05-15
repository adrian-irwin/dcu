/*
Author: Adrian Irwin
Date: 25/10/2021
This program finds the location of a given smaller string in a longer string.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Function:       searchSub
Parameters:     string to search through, string to find,
                pointer to integer that holds the location of where the string is found,
                pointer to integer that holds the end location of where the string is found
returns:        int
description:    Finds the location of a sub string in a string.
*/
void searchSub(char string1[], char string2[], int *startLocation, int *endLocation) {
    char *pFound = NULL;
    if (strstr(string1, string2))
    {
        pFound = strstr(string1, string2); // strstr gives us a pointer to the start of the word in the sentence
        *startLocation = pFound - string1; // because the pointer pFound will be at the location of where the word is found we can subtract the sentence from the pointer and get the start location
        *endLocation = *startLocation + strlen(string2) - 1; // to find the end location of the word we add on the length of the word we are looking for to the start location and subtract 1
    }
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Initialises the variables location and location end and their pointers, then we call searchSub to find the location of the sub string.
*/
int main(int argc, char*argv[]){
    int location, locationEnd;
    int *pLocation = &location;
    int *pLocationEnd = &locationEnd;

    searchSub(argv[1], argv[2], pLocation, pLocationEnd);

    printf("%d %d\n", location, locationEnd);

    return 0;
}