#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int duplicates(int numbers[], int length){
    int dupe = -1;
    for (int i = 0; i < length; i++)
    {
        for (int j = i + 1; j < length; j++)
        {
            if (numbers[i] == numbers[j])
            {
                dupe = numbers[j];
                break;
            }
        }
        if (dupe != -1)
        {
            break;
        }

    }
    return dupe;
}

int main(int argc, char*argv[]){
    int length = argc-1;
    int numbers[length];
    for (int i = 0; i < length; i++)
    {
        numbers[i] = atoi(argv[i+1]);
    }
    int duplicate = duplicates(numbers, length);
    if (duplicate != -1)
    {
        printf("%d\n", duplicate);
    }
    else
    {
        printf("no duplicated number\n");
    }

    return 0;
}