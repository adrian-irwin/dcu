#include <stdio.h>
#include <stdlib.h>

int maxNum (int numbers[], int length){

    int max = numbers[0];

    for (int i = 0; i < length; i++)
    {
        if (numbers[i] > max)
        {
            max = numbers[i];
        }
    }

    return max;
}

int main(int argc, char*argv[]){
    int length = argc-1;
    int numbers[length];

    for (int i = 0; i < length; i++)
    {
        numbers[i] = atoi(argv[i+1]);
    }

    int biggest = maxNum(numbers, length);
    printf("%d\n", biggest);

    return 0;
}