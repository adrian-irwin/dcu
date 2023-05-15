/*
Author: Adrian Irwin
Date: 28/10/2021
This program gets the details for a country and prints the details line by line.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// this allows us to not use struct every time we define a struct
typedef struct Country Country;

// this makes the Country structure
struct Country{
    char name[30];
    char capital[30];
    float population;
    int size;
};

/*
Function:       makeCountry
Parameters:     array of string arguments
returns:        Country
description:    takes details of a country and makes them into a Country structure.
*/
Country makeCountry(char *argv[]){
	Country country;
	strcpy(country.name, argv[1]);
	strcpy(country.capital, argv[2]);
	country.population = atof(argv[3]);
	country.size = atoi(argv[4]);
	return country;
}

/*
Function:       printCountry
Parameters:     a Country struct
returns:        void
description:    prints the details of a given country
*/
void printCountry(Country c1){
	printf("%s\n", c1.name);
	printf("%s\n", c1.capital);
	printf("%.2f million people\n", c1.population);
	printf("%d km2\n", c1.size);
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    calls printCountry function using makeCountry as an argument to print the country's details
*/
int main(int argc, char*argv[]){
	printCountry(makeCountry(argv));
	return 0;
}
