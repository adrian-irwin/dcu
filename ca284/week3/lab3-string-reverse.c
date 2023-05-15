#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void reverseString(char* input){
    int length = strlen(input);
    char reversed[50];
    for (int i = 0; i < length; i++)
    {
        reversed[i] = input[length-i-1];
    }
    strcpy(input, reversed);
}

int main(int argc, char *argv[]) {

    char word[50];
    strcpy(word, argv[1]);
    int length = strlen(word);

    reverseString(word);

    printf("%s\n", word);

    return 0;
}
