/*
Author: Adrian Irwin
Date: 06/11/2021
This program takes a list of students and prints the students that have higher than average grade in CSCE.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// this allows us to not use struct every time we define a Student struct
typedef struct Student Student;

// this makes the Student structure
// this is to make it easier to store the students
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
Function:       createStudents
Parameters:     a pointer to the list of students, the number of students, strings including the students details
returns:        void
description:    Adds the details of the students to the list of students
*/
void createStudents(Student *listOfStudents, int numOfAllStudents, char *details[]){
    for (int i = 0; i < numOfAllStudents; i++){
        *(listOfStudents + i) = makeStudent(details[(i * 3) + 1], details[(i * 3) + 2], details[(i * 3) + 3]);
    }
}

/*
Function:       findAverage
Parameters:     a pointer to the list of students, number of students
returns:        float
description:    returns the average grade across all the subjects
*/
float findAverage(Student *listOfStudents, int numOfAllStudents){
    float average = 0;
    //(72.4+69.5+50.6+88.5+48.7+66.82)/6
    for (int i = 0; i < numOfAllStudents; i++)
    {
        average += (listOfStudents + i)->grade;
    }
    average /= numOfAllStudents;
    return average;
}

/*
Function:       printOustanding
Parameters:     a pointer to the list of students, number of students, average grade across all subjects
returns:        void
description:    prints the details of all the students in the list who have a grade higher than the overall average in CSCE
*/
void printOustanding(Student *listOfStudents, int numOfAllStudents, float avg){
    for (int i = 0; i < numOfAllStudents; i++){
        if (!strcmp((listOfStudents + i)->programmes, "CSCE") && (listOfStudents + i)->grade > avg){
        printf("%s, %.2f\n", (listOfStudents + i)->name, (listOfStudents + i)->grade);
        }
    }
}

/*
Function:       Main
Parameters:     length of command line arguments, command line arguments
returns:        int
description:    Create a list of the students using calloc, then we find the average mark using averageGrade and assign it to a variable.
                We print the students with a grade higher than average in CSCE using printOutstanding, finally we print the overall average grade.
*/
int main(int argc, char*argv[]){
    int length = argc - 1;
    int numOfStudents = length / 3;

    Student *students = calloc(numOfStudents, sizeof(Student));
    if (!students){
        printf("Not enough memory!\n");
        free(students);
        students = NULL;
        exit(0);
    }

    createStudents(students, numOfStudents, argv);
    float averageGrade = findAverage(students, numOfStudents);
    printOustanding(students, numOfStudents, averageGrade);
    printf("Average grade: %.2f\n", averageGrade);
    free(students);
    students = NULL;
    return 0;
}