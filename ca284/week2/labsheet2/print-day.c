#include <stdio.h>
#include <stdlib.h>


int main(int argc, char*argv[1]){
    if (atoi(argv[1]) == 1)
    {
        printf("Sunday\n");
    }
    else if (atoi(argv[1]) == 2)
    {
        printf("Monday\n");
    }
    else if (atoi(argv[1]) == 3)
    {
        printf("Tuesday\n");
    }
    else if (atoi(argv[1]) == 4)
    {
        printf("Wednesday\n");
    }
    else if (atoi(argv[1]) == 5)
    {
        printf("Thursday\n");
    }
    else if (atoi(argv[1]) == 6)
    {
        printf("Friday\n");
    }
    else if (atoi(argv[1]) == 7)
    {
        printf("Saturday\n");
    }

    return 0;
}