#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]){

int length = atoi(argv[1]);
int width = atoi(argv[2]);

for(int i = 1; i <= length; ++i)
{
    for(int j = 1; j <= width; ++j)
    {
        printf("*");
    }
    printf("\n");
}
}