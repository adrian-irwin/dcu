/*
Author: Adrian Irwin
Date: 28/10/2021
This program gets the details for multiple countries and prints the details for them then prints the average population of them.
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
Parameters:     a Country struct
returns:        void
description:    prints the details of a given country
*/
void printCountry(Country c1){
	printf("%s\t\t\t", c1.name);
	printf("%s\t\t\t", c1.capital);
	printf("%d\t\t\t", c1.size);
	printf("%.2f\n", c1.population);
}

/*
Function:       populationAverage
Parameters:     list of countries, number of arguments
returns:        float
description:    loops through all the countries in the list and returns the average of the countries' populations.
*/
float populationAverage(Country loc[], int argc){
    float length = (argc - 1) / 4;
    float average = 0;
    float sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += loc[i].population;
    }
    average = sum / length;
    return average;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    prints a header, create a country array,
                loop through the number of countries and make the countries using makeCountry then add them to the array.
                print the countries by calling printCountry and print the average by calling populationAverage.
*/
int main(int argc, char*argv[]){
    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");
    Country countries[50];
    for (int i = 0; i < (argc - 1) / 4; i++)
    {
        countries[i] = makeCountry(argv[(i * 4) + 1], argv[(i * 4) + 2], argv[(i * 4) + 3], argv[(i * 4) + 4]);
        printCountry(countries[i]);
    }
    printf("Population average: %.2f\n", populationAverage(countries, argc));
	return 0;
}
