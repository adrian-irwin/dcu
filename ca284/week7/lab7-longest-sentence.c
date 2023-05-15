/*
Author: Adrian Irwin
Date: 06/11/2021
This program takes strings and prints the longest ones.
*/

// input = multiple strings
// find longest string

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Function:       findMax
Parameters:     pointer to the list, size of the list
returns:        float
description:    Finds the largest length in the list.
*/
int findMax(int *lengths, int size){
    int max = *lengths; // set max to be the first number in the list.

    for (int i = 0; i < size; i++){
        if (*(lengths + i) > max){ // if the number we are checking is larger than max we assing max to the current number
            max = *(lengths + i);
        }
    }
    return max;
}

/*
Function:       makeList
Parameters:     pointer to the list, size of the list, words to put their length into the list
returns:        void
description:    Makes a list that contains the given lengths of the given words.
*/
void makeList(int *lengths, int size, char *words[]){
    for (int i = 0; i < size; i++){
        *(lengths + i) = strlen(words[i+1]); // we add the length of the words to the list
    }

}

/*
Function:       printLongestWords
Parameters:     size of the list, pointer to the list, list of given words
returns:        float
description:    Finds the second largest number in the list.
*/
void printLongestWords(int size, int *lengths, char *words[]){
    int maxLength = findMax(lengths, size);
    for (int i = 0; i < size; i++){ // we loop through the list until we find a word that is equal in length to maxLength and we print those words
        if (maxLength == *(lengths + i)){
            printf("%s\n", words[i+1]);
        }
    }

}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    initalize a list using calloc then add the lengths of the given words to the list by calling makeList, lastly we print the longest words by calling printLongestWords
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    // use calloc to create the list for the numbers with enough memory for all the numbers
    int *wordLengths = calloc(length, sizeof(int));
    if (!wordLengths){ // if we cant make the list we stop the program and free the memory
        printf("Not enough memory!\n");
        free(wordLengths);
        wordLengths = NULL;
        exit(0);
    }
    makeList(wordLengths, length, argv);
    printLongestWords(length, wordLengths, argv);
    // before the program ends we free the memory that we used to make the list
    free(wordLengths);
    wordLengths = NULL;
    return 0;
}