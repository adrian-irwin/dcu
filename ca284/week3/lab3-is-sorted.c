#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void bubSort(int numbers[], int length){
    for (int i = 0; i < length - 1; i++)
    {
        for (int j = 0; j < length - i - 1; j++)
        {
            if (numbers[j] > numbers[j+1])
            {
                int temp = numbers[j];
                numbers[j] = numbers[j+1];
                numbers[j+1] = temp;
            }
        }
    }
}

int main(int argc, char*argv[]){
    int length = argc-1;
    int numbers[length];

    for (int i = 0; i < length; i++)
    {
        numbers[i] = atoi(argv[i+1]);
    }

    bubSort(numbers, length);

    for (int i=0; i < length; i++)
    {
        printf("%d\n", numbers[i]);
    }

    return 0;
}