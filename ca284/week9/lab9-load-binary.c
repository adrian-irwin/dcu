#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Student Student;

struct Student
{
    char name[30];
    char college[30];
    int age;
    float grade;
};

int main(int argc, char*argv[]){

    FILE *pfile = NULL;
    char *filename = "studentBinary.bin";

    pfile = fopen(filename, "rb");
    if(!pfile){
        printf("Unable to open %s.\n", filename);
    }

    Student student;
    int lenOfName, lenOfCollege;

    int read1 = fread(&lenOfName, sizeof(int), 1, pfile);
    int read2 = fread(student.name, sizeof(char), lenOfName, pfile);
    int read3 = fread(&lenOfCollege, sizeof(int), 1, pfile);
    int read4 = fread(student.college, sizeof(char), lenOfCollege, pfile);
    int read5 = fread(&student.age, sizeof(int), 1, pfile);
    int read6 = fread(&student.grade, sizeof(float), 1, pfile);

    fclose(pfile);

    printf("Name: %s\n", student.name);
    printf("College: %s\n", student.college);
    printf("Age: %d\n", student.age);
    printf("Grade: %.2f\n", student.grade);
    return 0;
}


