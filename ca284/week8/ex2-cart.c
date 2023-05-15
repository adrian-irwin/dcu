/*
Program: ex2-cart.c
Author: Adrian Irwin
Date: 11/11/2021
This program takes in information about items in a shopping cart and prints out what the item is, how many there are, how much it is and if it is on sale or not.
*/

// example input:   ./ex2-cart "Cucumber" 5 1.0 0 "Guinness" 4 2.5 0 "Tayto" 10 2 1
// example output:  Cucumber,5,1.00,No Sale
//                  Guinness,4,2.50,No Sale
//                  Tayto,10,2.00,On Sale

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Cart Cart;

struct Cart{
    char item[20];
    unsigned int amount;
    float price;
    int promo;
};

/*
Function:       createItems
Parameters:     pointer to the list of items to add the details to, pointer to the list of details to be added, number of items that will be put into the list of items.
returns:        void
description:    Adds details of items into list of items.
*/
void createItems(Cart *listOfItems, char *details[], int numberOfItems){
    for (int i = 0; i < numberOfItems; i++){
        strcpy(listOfItems[i].item, details[(i * 4) + 1]);
        listOfItems[i].amount = atoi(details[(i * 4) + 2]);
        listOfItems[i].price = atof(details[(i * 4) + 3]);
        listOfItems[i].promo = atoi(details[(i * 4) + 4]);
    }
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Create a list of items using the Cart struct, add items to the list using the createItems function. Print out all the items and their details including if they are on sale or not.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    int numItems = length / 4;
    Cart items[numItems];

    createItems(items, argv, numItems);

    for (int i = 0; i < numItems; i++){
        printf("%s,%d,%.2f,", items[i].item, items[i].amount, items[i].price);
        if (items[i].promo){
            printf("On Sale\n");
        }
        else{
            printf("No Sale\n");
        }
    }

    return 0;
}