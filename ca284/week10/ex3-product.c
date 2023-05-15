/*
Program: ex3-product.c
Author: Adrian Irwin
Date: 25/11/2021
This program creates a list of products containing the product code, origin country and price from the command line.
All products which have origin country of "Ireland" has the price increased by 20%.
The products and their information are printed line by line.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Product Product;

struct Product
{
    char code[30];
    char country[30];
    unsigned int price;
};

// we need functions to create the list of products, update the prices of the products and print the products.
void createProducts(Product *listOfProducts, char *details[], int numberOfProducts);
void updatePrices(Product *listOfProducts, int numberOfProducts);
void printProducts(Product *listOfProducts, int numberOfProducts);

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    makes a list of products using the command line arguments by calling createProducts,
                updates the prices of the products using updatePrices,
                prints the list of products using printProducts.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    int numProducts = length / 3;
    Product items[numProducts];

    createProducts(items, argv, numProducts);
    updatePrices(items, numProducts);
    printProducts(items, numProducts);
    return 0;
}
/*
Function:       createProducts
Parameters:     pointer to a list of products, details of the products, number of products in the list
returns:        void
description:    Adds products to the list of products using the given details
*/
void createProducts(Product *listOfProducts, char *details[], int numberOfProducts){
    for (int i = 0; i < numberOfProducts; i++){
        strcpy(listOfProducts[i].code, details[(i * 3) + 1]);
        strcpy(listOfProducts[i].country, details[(i * 3) + 2]);
        listOfProducts[i].price = atof(details[(i * 3) + 3]);
    }
}
/*
Function:       updatePrices
Parameters:     pointer to a list of products, number of products in the list
returns:        void
description:    Updates prices of the products based on the origin country.
*/
void updatePrices(Product *listOfProducts, int numberOfProducts){
    for (int i = 0; i < numberOfProducts; i++)
    {
        if (strcmp(listOfProducts[i].country, "Ireland") == 0){
            listOfProducts[i].price = listOfProducts[i].price * 1.2;
        }
    }

}
/*
Function:       printProducts
Parameters:     pointer to a list of products, number of products in the list
returns:        void
description:    Prints the details of products line by line.
*/
void printProducts(Product *listOfProducts, int numberOfProducts){
    for (int i = 0; i < numberOfProducts; i++)
    {
        printf("%s\n%s\n%d\n", listOfProducts[i].code, listOfProducts[i].country, listOfProducts[i].price);
    }

}