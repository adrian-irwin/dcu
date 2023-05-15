#include <stdio.h>
#include <stdlib.h>

#define PI 3.1415

int main(int argc, char *argv[2])
{
    if(argc == 1){
        printf("No input given!\n");
    }
    else if(argc == 2){
        printf("Two arguments needed!\n");
    }
    else if(atoi(argv[1]) < 0 || atoi(argv[2]) < 0){
        printf("The radious or height cannot be negative!\n");
    }
    else if(argc == 3){
	    int radius = atoi(argv[1]);
	    int height = atoi(argv[2]);

	    float area = (2*PI*radius*height) + (2*PI*(radius*radius));

        printf("%.2f\n", area);
    }
    return (0);
}
