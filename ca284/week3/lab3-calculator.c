#include <stdio.h>
#include <string.h>
#include <stdlib.h>

float multiply(float num1, float num2) { return num1 * num2; }

float divide(float num1, float num2) { return num1 / num2; }

int main(int argc, char *argv[3]) {
    if (argc < 4 || strcmp(argv[2], "0") == 0 || strcmp(argv[3], "0") == 0){
        printf("invalid\n");
    }
    else if (strcmp(argv[1], "multiply") == 0){
        printf("%f\n", multiply( atof(argv[2]), atof(argv[3]) ) );
    }
    else if (strcmp(argv[1], "divide") == 0){
        printf("%f\n", divide( atof(argv[2]), atof(argv[3]) ) );
    }
    else
    {
        printf("invalid\n");
    }
    return 0;
}
