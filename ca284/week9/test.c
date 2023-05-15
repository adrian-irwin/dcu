#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Student Student;

struct Student{
    char name[50];
    char college[40];
    int age;
    float grade;
};

int main()
{
    FILE *pfile = NULL;  // File pointer
    char *filename = "studentBinary.bin"; //So a binary file has an extension of '.bin'
    pfile = fopen(filename, "wb"); //open a file with a binary mode
    if(!pfile) //check if the open operation work correctly
    {
        printf("Error opening %s for writing. Program terminated.\n", filename);
        exit(1);
    }

    Student s;

    strcpy(s.name, "John");
    strcpy(s.college, "DCU");
    s.age = 22;
    s.grade = 87.50;

    int wcount1 = fwrite(s.name, 1, strlen(s.name), pfile);
    int wcount2 = fwrite(s.college, 1, strlen(s.college), pfile);
    int wcount3 = fwrite(&s.age, sizeof(int), 1, pfile);
    int wcount4 = fwrite(&s.grade, sizeof(float), 1, pfile);

    fclose(pfile); //close the file
    return 0;
}