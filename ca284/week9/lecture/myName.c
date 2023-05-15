#include<stdio.h>
#include<stdlib.h>

int main(int argc, char*argv[])
{
    FILE *pfile = NULL;
    char *filename = "myname.txt";
    pfile = fopen(filename, "w");
    if(!pfile)  // Open myname.txt to write it
        printf("Failed to open %s.\n", filename);

    fprintf(pfile,"%s", argv[1]);
    fclose(pfile);
	return 0;
}