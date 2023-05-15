#include <stdio.h>
#include <stdlib.h>


int main(int argc, char*argv[]){
    int length = argc - 1;
    int numbers[length];
    int count = 0;
    for (unsigned int i = 0; i < length; i++)
    {
        numbers[i] = atoi(argv[i + 1]);
    }

    for (unsigned int i = 0; i < length; i++)
    {
        if (numbers[i] % 2 == 1)
        {
            count += 1;
        }
    }
    printf("%d\n", count);

    return 0;
}