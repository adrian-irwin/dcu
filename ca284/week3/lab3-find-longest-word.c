// input == a sentence
// print the largest word in the sentence

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char*argv[]){
    int length = strlen(argv[1]);
    char sentence[length];
    strcpy(sentence, argv[1]);
    printf("%d\n", length);
    printf("%s\n", sentence);
    char tmp[length];
    int count = 0;
    for (int i = 0; i < length; i++){
        if (sentence[i] != " " || sentence[i] != "\0"){
            count++;
        }

    }

    return 0;
}