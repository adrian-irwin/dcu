
/*
Name: Adrian Irwin
Student Number: 20415624
I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy,
and any work that is either paraphrased, summarised or directly quoted from the work of others has been referenced.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include "functions.h"

#define MAX_BUFFER 1024                         // max line buffer
#define MAX_ARGS 64                             // max # args
#define SEPARATORS " \t\n"                      // token separators

extern char **environ;                          // environment variables

int main (int argc, char ** argv){
    signal(SIGCHLD, SIG_IGN);                   // register a signal handler for background children processes to be ignored
    char buf[MAX_BUFFER];
    char * args[MAX_ARGS];
    char ** arg;
    char path[MAX_BUFFER];                      // variable to store the path
    getcwd(path, MAX_BUFFER);       	        // get the current directory and store it in path
    setenv("shellPath", path, 1);               // store the path to myshell so it can be used for the help command
    strcat(path, "/myshell");                   // add '/myshell' to the path
    setenv("shell", path, 1);                   // store the location of the shell executable as environment variable 'shell'

    if (argc == 2){                             // if we have 2 args from command line it is batchmode
        if (access(argv[1], F_OK) == 0){        // if the file does exist
            freopen(argv[1], "r", stdin);       // open the file and make it our stdin
        }
        else {                                  // if the file does not exist, print an error
            printf("File (%s) does not exist.\n", argv[1]);
            exit(1);
        }
    }

    int input = 0, output = 0;

    while (!feof(stdin)) {
        getcwd(path, MAX_BUFFER);               // get the current dir and store it in path

        if ((input == 0 && output == 0) && argc != 2){      // if i/o redirection or batchmode, the prompt will not be printed
            printPrompt(path);
        }

        if (fgets(buf, MAX_BUFFER, stdin)) {
            arg = args;
            *arg++ = strtok(buf,SEPARATORS);

            while ((*arg++ = strtok(NULL,SEPARATORS)));

            int i = 0, outputFileIndex = 0;
            while (args[i]){                                // loop through the args to see if we have to do i/o redirection
                if (!strcmp(args[i], "<")){                 // if we find '<', use the file after the '<' as an input file
                    if (!access(args[i+1], R_OK)){
                        freopen(args[i+1], "r", stdin);
                        input = 1;
                    }
                }
                else if (!strcmp(args[i], ">")){            // if we find '>', use the file after the '>' as output
                    output = 1;
                    outputFileIndex = i + 1;
                }
                else if (!strcmp(args[i], ">>")){           // if we find '>>', use the file after the '>>' as output and append to the file
                    output = 2;
                    outputFileIndex = i + 1;
                }
                i++;
            }

            if (args[0]){
                checkCommands(args[0], path, args, output, outputFileIndex);

                if (input == 0){
                    output = 0;     // reset output to 0 so we get are able to get the prompt back.
                }
                continue;
            }
        }
    }


    return 0;
}