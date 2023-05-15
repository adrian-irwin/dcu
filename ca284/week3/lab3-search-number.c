#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int search(int searchFor, int numbers[], int length){
    int location;
    for (int i = 1; i <= length; i++)
    {
        if (numbers[i] == searchFor)
        {
            location = i;
        }
    }
    return location;
}

int main(int argc, char*argv[]){
    int length = argc-2;
    int numbers[length];
    int numToFind = atoi(argv[1]);

    for (int i = 0; i < length; i++)
    {
        numbers[i] = atoi(argv[i+2]);
    }

    int foundAt = search(numToFind, numbers, length);

    if (foundAt <= length && foundAt >= 0)
    {
        printf("Found %d at %d\n", numToFind, foundAt);
    }
    else
    {
        printf("%d not found\n", numToFind);
    }

    return 0;
}