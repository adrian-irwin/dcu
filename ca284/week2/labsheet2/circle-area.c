#include <stdio.h>
#include <stdlib.h>

#define PI 3.1415

int main(int argc, char*argv[1]){
    int radius;
    float area;

    radius = atoi(argv[1]);
    area = (radius * radius) * PI;

    printf("%.2f\n", area);
    return 0;
}