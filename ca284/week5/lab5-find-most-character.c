/*
Author: Adrian Irwin
Date: 24/10/2021
This program finds the letter that occurs most in a given string.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/*
Function:       characterCount
Parameters:     character to find, string to find the character in
returns:        int
description:    Finds all occurrences of character and adds that to count.
*/
int characterCount (char letter, char word[]){
    char *pWord = word;
    int count = 0;
    while (pWord = strchr(pWord, letter))
    {
        count++;
        pWord++;
    }
    return count;
}

/*
Function:       mostCharacter
Parameters:     string
returns:        int
description:    Finds the character that occurs the most by using countCharacter.
*/
char mostCharacter(char word[]){
    int length = strlen(word); // find the length of the string
    int max = 0; // make a max variable to store the character count with the most occurrences
    char most; // make a most variable to store the character with the most occurrences
    for (int i = 0; i < length; i++)
    {
        if (characterCount(word[i], word) > max && isalnum(word[i]) != 0)
        // if the count of characters is found to be more than the current max and is a letter or number, we make it the new max
        {
            max = characterCount(word[i], word); // overwrite the old max
            most = word[i]; // overwrite the old character with the newer character that has the most occurrances
        }
    }
    return most;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    calls on mostCharacter to print character found most times.
*/
int main(int argc, char*argv[]){
    printf("%c\n", mostCharacter(argv[1]));
    return 0;
}
