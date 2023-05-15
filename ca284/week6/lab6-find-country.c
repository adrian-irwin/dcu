/*
Author: Adrian Irwin
Date: 30/10/2021
This program gets the details for multiple countries and prints the details for them based on if the size of the country is under 100000 km2.
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
Parameters:     name of country, capital of country, population of country, size of country
returns:        Country
description:    takes details of a country and makes them into a Country structure.
*/
Country makeCountry(char name[], char capital[], char population[], char size[]){
	Country country;
	strcpy(country.name, name);
	strcpy(country.capital, capital);
	country.population = atof(population);
	country.size = atoi(size);
	return country;
}

/*
Function:       printCountry
Parameters:     a pointer to a Country struct
returns:        void
description:    prints the details of a given country if the size is under 100000 km2
*/
void printCountry(Country *c1){
	if (c1->size < 100000)
    {
        printf("%s\t\t\t", c1->name);
        printf("%s\t\t\t", c1->capital);
        printf("%d\t\t\t", c1->size);
        printf("%.2f\n", c1->population);
    }

}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    prints a header, create a country array,
                loop through the number of countries and make the countries using makeCountry then add them to the array.
                print the countries by calling printCountry.
*/
int main(int argc, char*argv[]){
    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");
    Country countries[50];
    for (int i = 0; i < (argc - 1) / 4; i++){
        countries[i] = makeCountry(argv[(i * 4) + 1], argv[(i * 4) + 2], argv[(i * 4) + 3], argv[(i * 4) + 4]);

        printCountry(&countries[i]);
    }

	return 0;
}
