#include <stdio.h>

int main(int argc, char*argv[]){

    float centimetre;
    printf("Input an amount of centimetres to convert: ");
    scanf("%f", &centimetre);

    float inch = centimetre / 2.54;

    printf("Converted to inches: %f\n", inch);

    return(0);
}