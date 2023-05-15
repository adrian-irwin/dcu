/*
Author: Adrian Irwin
Date: 06/11/2021
This program takes a list of students and prints them if there is more than two students.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// this allows us to not use struct every time we define a Student struct
typedef struct Student Student;

// this makes the Student structure
// this is too make it easier to store the students
struct Student{
    char name[20];
    char programmes[20];
    float grade;
};

/*
Function:       makeStudent
Parameters:     string for the name of student, string for the name of subject, grade they got in the subject
returns:        Student
description:    Makes a student struct using the given details
*/
Student makeStudent(char name[], char programmes[], char grade[]){
	Student student;
	strcpy(student.name, name);
	strcpy(student.programmes, programmes);
	student.grade = atof(grade);
	return student;
}
/*
Function:       firstTwoStudents
Parameters:     a pointer to a list of students, strings including the students details
returns:        void
description:    adds the details of the first two students to a list of students
*/
void firstTwoStudents(Student *listOfStudents, char *details[]){
    for (int i = 0; i < 2; i++){
        *(listOfStudents + i) = makeStudent(details[(i * 3) + 1], details[(i * 3) + 2], details[(i * 3) + 3]);
    }
}
/*
Function:       addTheRestStudents
Parameters:     a pointer to the list of students, the number of students, strings including the students details
returns:        void
description:    adds the details of the rest of the students to the list of students
*/
void addTheRestStudents(Student *listOfStudents, int numOfAllStudents, char *details[]){
    for (int i = 2; i < numOfAllStudents; i++){
        *(listOfStudents + i) = makeStudent(details[(i * 3) + 1], details[(i * 3) + 2], details[(i * 3) + 3]);
    }
}
/*
Function:       printStudents
Parameters:     a pointer to the list of students, number of students
returns:        void
description:    prints the details of all the students in the list
*/
void printStudents(Student *listOfStudents, int numOfAllStudents){
    for (int i = 0; i < numOfAllStudents; i++){
        printf("%s, %s, %.2f\n", (listOfStudents + i)->name, (listOfStudents + i)->programmes, (listOfStudents + i)->grade);
    }
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Create a list for the first two students using calloc then add the first two students using the firstTwoStudents function,
                then we check if there is more than two students, if there is we use realloc to create a new list with the values of the first two students but with space to add the rest.
                We add the rest of the students using addTheRestStudents and then print all the students using printStudents.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    int numOfStudents = length / 3;
    Student *students = calloc(2, sizeof(Student)); // create a student list using calloc to hold 2 items
    if (!students){
        printf("Not enough memory!\n");
        free(students);
        students = NULL;
        exit(0);
    }
    firstTwoStudents(students, argv);

    if (numOfStudents > 2){
        Student *restOfStudents = realloc(students, numOfStudents * sizeof(Student));
        if (!restOfStudents){
            printf("Not enough memory!\n");
            free(restOfStudents);
            restOfStudents = NULL;
            exit(0);
        }
        students = restOfStudents; // after using realloc to create more space we have to reassign students to the new piece of memory.

        addTheRestStudents(students, numOfStudents, argv);
        printStudents(students, numOfStudents);
        free(students);
        students = NULL;
    }

    free(students);
    students = NULL;
    return 0;
}