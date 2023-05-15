/*
Program: ex2-receipt.c
Author: Adrian Irwin
Date: 11/11/2021
This program takes in information about items in a shopping cart and prints out how much the shopping cart will cost factoring in any discounts.
*/

// example input:   ./ex2-cart "Cucumber" 5 1.0 0 "Guinness" 4 2.5 0 "Tayto" 10 2 1
// example output:  29

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
Function:       discount
Parameters:     pointer to a single Cart item.
returns:        float
description:    Finds out the price of the items after factoring in the discounts.
*/
float discount(Cart *item){
    int leftover = (item->amount % 3); // find the items that will not count for the discount
    int freeProducts = item->amount / 3; // these products are the ones that we will not have to pay for
    int productsToPay = (item->amount - leftover - freeProducts); // we find the actual amount of products that we will have to pay for not including the free items and the items that dont count to the discount.
    int priceAfterDiscount = (leftover * item->price) + (productsToPay * item->price);
    return priceAfterDiscount;
}

/*
Function:       sumAmount
Parameters:     pointer to the list of items, number of items in the list.
returns:        float
description:    Finds the full total cost of all the items in the cart, finds the cost of items that have discounts by calling the discount function.
*/
float sumAmount(Cart *listOfItems, int numberOfItems){
    int sum = 0;
    for (int i = 0; i < numberOfItems; i++){
        if (!listOfItems[i].promo){ // if there is no promotion on the item we just find the cost without finding out the discount.
            sum += (listOfItems[i].amount * listOfItems[i].price);
        }
        else{
            sum += discount(&listOfItems[i]);
        }
    }
    return sum;
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Create a list of items using the Cart struct, then finds ands prints the full cost of the cart by calling the sumAmount function.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    int numItems = length / 4;
    Cart items[numItems];

    createItems(items, argv, numItems);

    float sum = sumAmount(items, numItems);
    printf("%.2f\n", sum);
    return 0;
}