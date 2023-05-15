#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define MAX_BUFFER 1024                        // max line buffer
#define MAX_ARGS 64                            // max # args
#define SEPARATORS " \t\n"                     // token separators

extern char **environ;
extern int errno;
void syserr(char*);


int main (int argc, char ** argv){
    pid_t pid;
    // int rc;

    pid = getpid();
    printf("Process ID before fork: %d\n", pid);

    switch (fork()) {
        case -1:
            syserr("fork");
        case 0:             // execution in child process
            pid = getpid();  // get child pid
            printf("Process ID in child after fork: %d\n", pid);
            execlp("sleepy", "sleepy", "10",NULL);
            syserr("execl"); // error if return from exec
    }

    pid = getpid();
    printf("Process ID after fork: %d\n", pid);

    char buf[MAX_BUFFER];                      // line buffer
    char * args[MAX_ARGS];                     // pointers to arg strings
    char ** arg;                               // working pointer thru args
    char * prompt = "==> " ;                    // shell prompt
    /* keep reading input until "quit" command or eof of redirected input */

    while (!feof(stdin)) {
        char path[MAX_BUFFER];
        getcwd(path, MAX_BUFFER);
        fputs(path, stdout);
        fputs(" : ", stdout);
        /* get command line from input */
        fputs(prompt, stdout); // write prompt

        if (fgets (buf, MAX_BUFFER, stdin )) { // read a line
            /* tokenize the input into args array */
            arg = args;
            *arg++ = strtok(buf,SEPARATORS);   // tokenise input

            while ((*arg++ = strtok(NULL,SEPARATORS)));

            // last entry will be NULL
            if (args[0]) {                     // if there's anything there
                /* check for internal/external command */
                if (!strcmp(args[0],"clr")) { // "clear" command
                    system("clear");
                    continue;
                }

                if (!strcmp(args[0],"quit")){   // "quit" command
                    exit(0);
                }

                if (!strcmp(args[0], "dir")){
                    char dir[MAX_BUFFER] = "ls -al '";
                    strcat(dir, path);
                    strcat(dir, "'");
                    system(dir);
                    continue;
                }

                if (!strcmp(args[0], "environ")){
                    int i = 0;
                    while (environ[i])
                    {
                        printf("%s\n", environ[i++]);
                    }
                    continue;
                }

                if (!strcmp(args[0], "cd")){
                    if (!args[1]){
                        printf("%s\n", path);
                    } else {
                        chdir(args[1]);
                        char newPath[MAX_BUFFER];
                        getcwd(newPath, MAX_BUFFER);
                        printf("newPath = %s\n", newPath);
                        char newPWD[MAX_BUFFER] = "PWD=";
                        strcat(newPWD, newPath);
                        printf("newPWD = %s\n", newPWD);
                        putenv(newPWD);
                    }
                    continue;
                }


                /* else pass command onto OS (or in this instance, print them out) */
                arg = args;
                while (*arg) {
                    system(*arg++);
                }
        }
    }
    return 0;
}}

void syserr(char * msg) {
    fprintf(stderr, "%s: %s", strerror(errno), msg);
    abort();
}