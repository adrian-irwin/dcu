/*
Program: ex4-attendance.c
Author: Adrian Irwin
Date: 10/12/2021
This program accepts n attendance records for n students. The records are a sequence of characters that include 'P' for Present, 'A' for Absent and 'L' for Late. If the student has more than 3 absences or 3 consecutive lates they will have an attendance status of 1, Otherwise the student will have an attendance staus of 0.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// function prototypes
void changeStatus(int *status, int size, char *words[]);
int absentCount(char*list[], int size, int i);
int findLates(char*list[], int size, int i);
void printStatus(int *list, int size);

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Makes an array using memory allocation to store the status of the student's attendance.
                Call changeStatus to adjust the status of the student's attendance.
                Call printStatus to print all of the statuses.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    int *status = (int*)calloc(length, sizeof(int));
    if (!status){
        printf("Not enough memory!\n");
        exit(0);
    }
    changeStatus(status, length, argv);
    printStatus(status, length);
    return 0;
}

/*
Function:       changeStatus
Parameters:     list of student attendance statuses, size of the list, current place in list
returns:        void
description:    Change student attendance statuses based on their absences and lates.
*/
void changeStatus(int *status, int size, char *words[]){
    for (int i = 0; i < size; i++){
        int absences = absentCount(words, size, i);
        int lateCheck = findLates(words, size, i);
        if (absences >= 3){
            *(status + i) = 1;
        }
        else if (lateCheck == 1){
            *(status + i) = 1;
        }
    }
}

/*
Function:       absentCount
Parameters:     list of student attendance records, size of the list, current place in list
returns:        int
description:    Count the number of absences a student has.
*/
int absentCount(char*list[], int size, int i){
    char *finder = *(list + i + 1);
    finder = strchr(*(list + i + 1), 'A');
    int count = 0;
    while (finder != NULL){
        count++;
        finder++;
        finder = strchr(finder, 'A');
    }
    return count;
}

/*
Function:       findLates
Parameters:     list of student attendance records, size of the list, current place in list
returns:        int
description:    Check if the current student record has 3 conesecutive lates.
*/
int findLates(char*list[], int size, int i){
    int count = 0;
    if (strstr(*(list + i + 1), "LLL")){
        count = 1;
    }

    return count;
}



/*
Function:       printStatus
Parameters:     list of student attendance statuses, size of the list
returns:        void
description:    Prints all the student attendance statuses.
*/
void printStatus(int *list, int size){
    for (int i = 0; i < size; i++){
        printf("%d\n", *(list + i));
    }
}