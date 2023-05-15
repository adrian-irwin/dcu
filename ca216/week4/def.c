#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include <sys/wait.h>

#define MAX_BUFFER 1024                        // max line buffer
#define MAX_ARGS 64                            // max # args
#define SEPARATORS " \t\n"                     // token separators

extern char **environ;

void clearTerminal();

pid_t pid;
pid_t cpid;
int status;

int main (int argc, char ** argv){
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
                    // system("clear");
                    // execlp("clear", "clear", NULL);
                    clearTerminal();
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

                if (!strcmp(args[0], "test"))
                {
                    pid = fork();
                    if (pid < 0){
                        printf("can't fork, error occured\n");
                        exit(1);
                    }
                    else if (pid == 0){

                        // pid == 0 means child process created
                        // getpid() returns process id of calling process
                        // Here It will return process id of child process
                        printf("child process, pid = %u\n",getpid());
                        // Here It will return Parent of child Process means Parent process it self
                        printf("parent of child process, pid = %u\n",getppid());

                        // the argv list first argument should point to
                        // filename associated with file being executed
                        // the array pointer must be terminated by NULL
                        // pointer
                        // char * argv_list[] = {"ls","-lart","/home",NULL};

                        // the execv() only return if error occured.
                        // The return value is -1
                        // execv("ls",argv_list);
                        execlp("ls", "ls", "-lh", ".", NULL);
                        // execlp("clear", "clear", NULL);
                        sleep(4);
                        exit(0);
                    }
                    else{
                        printf("parent process, pid = %u\n",getpid());
                        cpid = wait(&status);
                        printf("Child complete (pid=%d) with status = %d\n", cpid, status);
                        continue;
                    }

                /* else pass command onto OS */
                arg = args;
                while (*arg) {
                    system(*arg++);
                    continue;
                }
            }
        }
    return 0;
}}}

void clearTerminal() {
    pid = fork();
    if (pid < 0){
        printf("can't fork, error occured\n");
        exit(1);
    }
    else if (pid == 0){
        // pid == 0 means child process created
        printf("child process, pid = %u\n",getpid());
        printf("parent of child process, pid = %u\n",getppid());

        // the execlp() only return if error occured.
        // The return value is -1
        execlp("clear", "clear", NULL);
        sleep(4);
        exit(0);
    }
    else{
        printf("parent process, pid = %u\n",getpid());
        wait(&status);
        // printf("Child complete (pid=%d) with status = %d\n", cpid, status);
    }
}