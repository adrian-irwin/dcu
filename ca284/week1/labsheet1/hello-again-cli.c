#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]){

    char *name;

    name = argv[1];

    printf("Hello %s\n", name);

    return(0);
}