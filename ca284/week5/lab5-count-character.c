/*
Author: Adrian Irwin
Date: 24/10/2021
This program count the amount of times that a given character is found in a given string.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Function:       characterCount
Parameters:     character to find, string to find the character in
returns:        int
description:    Finds all occurrences of character and adds that to count.
*/
int characterCount (char letter, char word[]){
    char *pWord = word; // use a pointer to point at the start of the string we are searching
    int count = 0; // make a count of times the letter is found
    while (pWord = strchr(pWord, letter)) // as long as strchr doesn't return NULL then we assign pWord to strchr(pWord, letter)
    {
        count++;
        pWord++; // add one to pWord so we don't find the same letter again in the next iteration of the loop
        // without this we would have an infinite loop
    }
    return count;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    calls on characterCount to print the number of times we find character.
*/
int main(int argc, char*argv[]){
    // argv[1] = character
    // argv[2] = string to find character
    printf("%d\n", characterCount(*argv[1], argv[2]));

    return 0;
}
