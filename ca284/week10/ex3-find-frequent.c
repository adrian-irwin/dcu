/*
Program: ex3-find-frequent.c
Author: Adrian Irwin
Date: 25/11/2021
This program creates a list of integers from the command line.
All numbers that occur more than 3 times are added to a new list and printed out line by line.
*/

#include <stdio.h>
#include <stdlib.h>

// allocate memory for 5 integers
// if the memory need goes over 5 add additional memory
// find all elements that occur more than 3 times in a new array with enough memory for all the elements
// print all the elements out


//functions are need to make the list, count the occurrences of a number in the list, find how long the second list will need to be, make the second list, sort the list and print the list.
void makeList(int size, char *numbers[], int *list);
int occurrences(int *list, int size, int find);
int findSecondLength(int *oldList, int size);
void makeSecondList(int size, int oldListSize, int *oldList, int *newList);
void printList(int *list, int size);
void bubSort(int *list, int size);

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    make a list of numbers using the command line arguments using memory allocation and calling makeList,
                we find the length of the second list using findSecondLength,
                make a second list of numbers that has numbers that occur more than 3 times using memory allocation and calling makeSecondList,
                sort the list using bubSort and print the list using printList.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;

    int *pList = (int*)calloc(5, sizeof(int));
    if(!pList){
        printf("Not enough memory!");
        exit(0);
    }

    makeList(length, argv, pList);

    int secondListLength = findSecondLength(pList, length);
    int *secondList = (int*)calloc(secondListLength, sizeof(int));
    if(!secondList){
        printf("Not enough memory!");
        exit(0);
    }
    makeSecondList(secondListLength, length, pList, secondList);
    free(pList);
    pList = NULL;

    bubSort(secondList, secondListLength);
    printList(secondList, secondListLength);

    free(secondList);
    secondList = NULL;
    return 0;
}

/*
Function:       makeList
Parameters:     length of the list, numbers to be put into the list, pointer to the list
returns:        void
description:    Adds integers to list of numbers using given integers
*/
void makeList(int size, char *numbers[], int *list){
    for (int i = 0; i < 5; i++){
        *(list + i) = atoi(numbers[i + 1]);
    }
    int *temp = NULL;
    if (size > 5){
        for (int i = 5; i < size; i++){
            temp = realloc(list, (i + 1)*sizeof(int));
            if(!temp){
                printf("Not enough memory!");
                free(list);
                list = NULL;
            }
        	list = temp;

            *(list + i) = atoi(numbers[i + 1]);
        }
    }
}

/*
Function:       occurrences
Parameters:     pointer to the list, length of the list, integer to find in the list
returns:        int
description:    returns the number of times a given integer is found in the list.
*/
int occurrences(int *list, int size, int find){
    int count = 0;
    for (int i = 0; i < size; i++)
    {
        if (find == *(list + i))
        {
            count++;
        }

    }
    return count;
}

/*
Function:       findSecondLength
Parameters:     pointer to a list, length of the list
returns:        int
description:    returns the length needed to make the second list.
*/
int findSecondLength(int *oldList, int size){
    int num = 0;
    for (int i = 0; i < size; i++)
    {
        int timesFound = occurrences(oldList, size, *(oldList + i));
        if (timesFound > 3)
        {
            num++;
        }
    }
    return num;
}

/*
Function:       makeSecondList
Parameters:     length of the new list, length of the old list, pointer to the old list, pointer to the new list.
returns:        void
description:    Adds integers to the new list if they occur more than 3 times.
*/
void makeSecondList(int size, int oldListSize, int *oldList, int *newList){
    int num = 0;
    for (int i = 0; i < oldListSize; i++)
    {
        int timesFound = occurrences(oldList, oldListSize, *(oldList + i));
        if (timesFound > 3)
        {
            *(newList + num) = *(oldList + i);
            num++;
        }
    }

}

/*
Function:       printList
Parameters:     pointer to the list, length of the list,
returns:        void
description:    Prints the given list
*/
void printList(int *list, int size){
    for (int i = 0; i < size; i++)
    {
        printf("%d\n", *(list + i));
    }

}

/*
Function:       bubSort
Parameters:     pointer to the list, length of the list,
returns:        void
description:    Sorts the given list in ascending order.
*/
void bubSort(int *list, int size){
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - i - 1; j++)
        {
            if (*(list +j) > *(list + j+1))
            {
                int temp = *(list +j);
                *(list +j) = *(list + j+1);
                *(list + j+1) = temp;
            }
        }
    }
}