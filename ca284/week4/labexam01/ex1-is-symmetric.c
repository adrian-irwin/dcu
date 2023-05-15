/*
Author: Adrian Irwin
Date: 15/10/2021
This program checks if the given string is symmetric or not.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Function:       symmetric
Parameters:     word
returns:        int
description:    Finds if the string inputted is symmetric or not.
*/
int symmetric(char word[]){
    int i = 0, count = 0;
    while (i < strlen(word) / 2) // run until i gets to the halfway point of the string
    {
        if (word[i] == word[strlen(word) - 1 - i]) // if i is equal to the character on the opposite end of the string add one to count
        {
            count++;
        }
        i++;
    }

    int out;
    if (count == strlen(word) / 2)// if "count" is equal to half of the len of word we know that each letter on one side of the string was equal to the other side
    {
        out = 1;
    }
    else
    {
        out = 0;
    }

    return out;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Checks if a given string is symmetric based off output from symmetric function.
*/
int main(int argc, char*argv[]){
    int check;
    char word[50];
    strcpy(word, argv[1]); // copy the word to a variable

    check = symmetric(word);
    if (check == 1) // if check equals 1 then the string is symmetric
    {
        printf("yes\n");
    }
    else
    {
        printf("no\n");
    }

    return 0;
}