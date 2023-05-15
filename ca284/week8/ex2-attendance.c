/*
Program: ex2-attendance.c
Author: Adrian Irwin
Date: 11/11/2021
This program takes students attendance records and students will not be awarded for attendance (print '0') if they have more than two absences,
otherwise students will be awarded for attendance (print '1').
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Function:       absentCount
Parameters:     pointer to students attendance records, the studentCount to identify the student
returns:        int
description:    Returns the amount of absences a given student has.
*/
int absentCount(char *record[], int studentCount){
    char *finder = *(record + studentCount + 1);
    finder = strchr(*(record + studentCount + 1), 'A');
    int count = 0;
    while (finder != NULL){
        finder++;
        count++;
        finder = strchr(finder, 'A');
    }
    return count;
}

/*
Function:       attendance
Parameters:     list to store attendance awards, pointer to students attendance records, total of students that have attendance records
returns:        void
description:    Makes an array containing the attendance records of all the students, absentCount is used to determine if a student has more than 2 absences.
*/
void attendance(int list[], char *record[], int size){
    for (int i = 0; i < size; i++){
        int count = absentCount(record, i);
        if (count > 2){ // if a student has more than two absences then they are given a 0 mark.
            list[i] = 0;
        }
        else{ // students are given a 1 mark if they have less than two absences.
            list[i] = 1;
        }
    }
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Makes an array that contains the students attendance awards and is populated using the attendance function, which is then printed out.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    int attRecord[length];
    attendance(attRecord, argv, length);
    for (int i = 0; i < length; i++){
        printf("%d\n", attRecord[i]);
    }

    return 0;
}