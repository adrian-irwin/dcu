#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int oddNums (int numbers[], int length){
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        if (numbers[i] % 2 == 1)
        {
            sum += numbers[i];
        }

    }
    return sum;
}
int evenNums (int numbers[], int length){
    int sum = numbers[0];
    for (int i = 1; i < length; i++)
    {
        if (numbers[i] % 2 == 0)
        {
            sum -= numbers[i];
        }

    }
    return sum;
}



int main(int argc, char*argv[]){
    int length = argc - 1;
    int list1[length];
    for (int i = 0; i < length; i++)
    {
        list1[i] = atoi(argv[i+1]);
    }

    int odd = oddNums(list1, length);
    int even = evenNums(list1, length);

    printf("%d\n", odd);
    printf("%d\n", even);

    return 0;
}