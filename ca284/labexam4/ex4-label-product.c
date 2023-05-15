/*
Program: ex4-label-product.c
Author: Adrian Irwin
Date: 10/12/2021
This program accepts information about items in a cart at a shop. The first two letters in the code relate to the country.
The program prints the status and country of each item.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Product Product;

struct Product{
    char code[20];
    float price;
    unsigned int numberSold;
    int status;
    Product *next;
};

// function prototypes
Product* createProducts(char*info[], int size);
float findAverageSales(Product *start);
void changeStatus(Product *start, float average);
void printList(Product *start);

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Create an array of products by calling createProducts.
                Change the status of each proudct by calling changeStatus.
                Print the list of products by calling printList.
*/
int main(int argc, char*argv[]){
    int numberOfItems = (argc - 1) / 3;
    Product *start = createProducts(argv, numberOfItems);
    float avg = findAverageSales(start);
    changeStatus(start, avg);
    printList(start);
    return 0;
}

/*
Function:       createProducts
Parameters:     details to put into the list, size of the details
returns:        Product*
description:    Create a list of products using the given details.
*/
Product* createProducts(char*info[], int size){
    Product *current, *first;
    first = (Product*)calloc(1,sizeof(Product));
    if (!first){
        printf("Not enough memory!\n");
        exit(0);
    }
    current = first;
    strcpy(current->code, info[1]);
    current->price = atof(info[2]);
    current->numberSold = atoi(info[3]);
    for (int i = 1; i < size; i++){
        current->next = (Product*)calloc(1,sizeof(Product));

        current = current->next;

        strcpy(current->code, info[(i * 3) + 1]);
        current->price = atof(info[(i * 3) + 2]);
        current->numberSold = atoi(info[(i * 3) + 3]);
        current->status = 0;
    }
    current->next = NULL;

    return first;
}

/*
Function:       findAverageSales
Parameters:     details to put into the list, size of the details
returns:        float
description:    Returns the average amount of sales of all items
*/
float findAverageSales(Product *start){
    float sum = 0.0;
    int count = 0;
    for (; start != NULL; start = start->next){
        sum += start->price * start->numberSold;
        count++;
    }
    float average = sum / count;
    return average;
}

/*
Function:       changeStatus
Parameters:     list of products, average sales of the items
returns:        void
description:    changes the status of an item if its sales are above the average sales.
*/
void changeStatus(Product *start, float average){
    for (; start != NULL; start = start->next){
        float sales = start->price * start->numberSold;
        if (sales >= average){
            start->status = 1;
        }
    }
}

/*
Function:       printList
Parameters:     list of products
returns:        void
description:    prints the status and country for each item.
*/
void printList(Product *start){
    char codes[5][3] = {"IE","FR","SP","US","RU"};
    char countries[5][8] = {"Ireland", "France", "Spain", "USA", "Russia"};
    for (; start != NULL; start = start->next){
        printf("%d\n", start->status);
        char countryCode[3];

        for (int i = 0; i < 2; i++){
            countryCode[i] = start->code[i];
        }
        int countryIndex = -1;
        for (int i = 0; i < 5; i++){
            if (strcmp(countryCode, codes[i]) == 0){
                countryIndex = i;
            }
        }
        printf("%s\n", countries[countryIndex]);
    }
}
