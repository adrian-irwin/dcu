/*
 circle-area.c
 author <your name>
*/

#include <stdio.h>
#include <stdlib.h>

#define PI 3.1415

int main(int argc, char *argv[1])
{
    for (int i = 1; i <= atoi(argv[1]); ++i){
        for (int j = 1; j <= atoi(argv[1]); ++j){
            if (i == 1 || j == 1 || i == atoi(argv[1]) || j == atoi(argv[1])){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
    return (0);
}
