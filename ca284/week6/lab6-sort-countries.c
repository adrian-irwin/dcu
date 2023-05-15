/*
Author: Adrian Irwin
Date: 31/10/2021
This program gets the details for multiple countries, sorts them by population and prints the details of the countries.
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
Function:       sortCountries
Parameters:     a pointer to a Country struct, integer of the number of countries
returns:        void
description:    sorts the countries in the given country pointer by population
*/
void sortCountries(Country *country, int num){
    Country tmp; // create a temp country to store the previous country
    for (int i = 0; i < num; i++){ // loop until we reach the num
        for (int j = i + 1; j < num; j++){ // loop until we reach num starting after the first loop
            if (country[i].population < country[j].population){
                // if country in the first position has a lower population than the one after it we switch the two countries around so we can sort from highest to lowest
                tmp = country[i];
                country[i] = country[j];
                country[j] = tmp;
            }
        }
    }
}

/*
Function:       printCountry
Parameters:     a Country struct
returns:        void
description:    prints the details of a given country
*/
void printCountry(Country *c1){
	printf("%s\t\t\t", c1->name);
	printf("%s\t\t\t", c1->capital);
	printf("%d\t\t\t", c1->size);
	printf("%.2f\n", c1->population);
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    prints a header, create a country array,
                loop through the number of countries and make the countries using makeCountry then add them to the array.
                call the sort countries function to sort the countries by the population.
                print the countries by calling printCountry.
*/
int main(int argc, char*argv[]){
    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");
    Country countries[50];
    int numberOfCountries = (argc - 1) / 4;
    for (int i = 0; i < numberOfCountries; i++){
        countries[i] = makeCountry(argv[(i * 4) + 1], argv[(i * 4) + 2], argv[(i * 4) + 3], argv[(i * 4) + 4]);
    }
    sortCountries(countries, numberOfCountries);
    for (int i = 0; i < numberOfCountries; i++){
        printCountry(&countries[i]);
    }

    return 0;
}
