
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
#include <sys/wait.h>
#include <sys/stat.h>
#include <termios.h>
#include "functions.h"

#define MAX_BUFFER 1024                         // max line buffer

extern char **environ;                          // environment variables

// variables for forking
pid_t pid;
int status;

char * prompt = "MyShell> ";

void printPrompt(char * path){
    fprintf(stdout, "%s", path);                // print path to stdout
    fprintf(stdout, " : ");                     // separator between path and prompt
    fprintf(stdout, "%s", prompt);              // print prompt to stdout
}

/* Checks if the user input is an internal command.
If it is not an internal command we pass it to otherCommands and try to execute the command.
*/
void checkCommands(char * command, char * path, char ** args, int outputType, int outputIndex){

    if (!strcmp(command, "clr")){
        clearShell();
    }
    else if (!strcmp(command, "quit") || !strcmp(command, "exit")){
        printf("Exiting Shell.\n");
        exit(0);
    }
    else if (!strcmp(command, "environ")){
        printEnviron(environ, args, outputType, outputIndex);
    }
    else if (!strcmp(command, "cd")) {
        changeDirectory(path, args);
    }
    else if (!strcmp(command, "dir")){
        dir(path, args, outputType, outputIndex);
    }
    else if (!strcmp(command, "echo")){
        echo(args, outputType, outputIndex);
    }
    else if (!strcmp(command, "pause")){
        pauseShell(args);
    }
    else if (!strcmp(command, "help")){
        help(args, outputType, outputIndex);
    }
    else {
        otherCommands(command, args);
    }
}

/* Clears the shell */
void clearShell(){
    pid = fork();                                       // create a child process
    if (pid < 0){                                       // if pid returns anything under 0 it fails
        fprintf(stderr, "Error, Unable to fork.\n");
        exit(1);                                        // exit with a status of 1 after fail
    }
    else if (pid == 0){
        execlp("clear", "clear", NULL);                 // execute the clear command
        exit(0);                                        // exit with a status of 0
    }
    else {
        wait(&status);
    }
}

/* Prints all envirnonment variables */
void printEnviron(char ** envArray, char ** args, int outputType, int outputIndex){
    pid = fork();                                       // create a child process
    if (pid < 0){                                       // if pid returns anything under 0 it fails
        fprintf(stderr, "Error, Unable to fork.\n");
        exit(1);                                        // exit with a status of 1 after fail
    }
    else if (pid == 0){
        if (outputType == 1){
            freopen(args[outputIndex], "w", stdout);    // if outputType is 1 then we are writing to a file and truncating
        }
        else if (outputType == 2){
            freopen(args[outputIndex], "a", stdout);    // if outputType is 2 then we are appending to the end of a file
        }
        int i = 0;
        while (envArray[i]){                            // loop through the environment array while there is a still a value at position i
            printf("%s\n", envArray[i++]);
        }
        exit(0);
    }
    else {
        wait(&status);
    }
}

/* Check if given argument is a directory */
int checkDirectory(char * directory){
    struct stat stats;                                  // stat struct to store information about directory
    stat(directory, &stats);                            // use stat() to get the file attributes from directory and store them in stats
    if (S_ISDIR(stats.st_mode)){                        // check if 'directory' is a directory with S_ISDIR
        return 0;                                       // if it is a directory return 0
    }
    return 1;                                           // return 1 if it is not a directory
}

/* Changes the shell directory and updates the 'PWD' environment variable */
void changeDirectory(char * path, char ** args){

    if (!args[1]){
        fprintf(stdout, "The current directory is:\n%s \n", path);
    }
    else if (checkDirectory(args[1]) == 0){             // check if the given argument is a directory using checkDirectory()
        chdir(args[1]);                                 // change directory
        char newPath[MAX_BUFFER];                       // create new variable to store new path
        getcwd(newPath, MAX_BUFFER);                    // get new path and store it in newPath
        setenv("PWD", newPath, 1);                      // set "PWD" env to the new path
    }
    else {
        fprintf(stderr, "Unable to find given directory.\n");
    }
}

/* Prints out the contents of a directory */
void dir(char * path, char ** args, int outputType, int outputIndex){

    pid = fork();                                       // create a child process
    if (pid < 0){                                       // if pid returns anything under 0 it fails
        fprintf(stderr, "Error, Unable to fork.\n");
        exit(1);                                        // exit with a status of 1 after fail
    }
    else if (pid == 0){
        // if there is no arg at args[1] or the first arg is '>' or '>>', dir for current path
        // have to include strcmp for > and >> so that we dont call dir on the directory > and >>
        if (!args[1] || !(strcmp(args[1], ">") || !strcmp(args[1], ">>"))){
            if (outputType == 1){                       // if outputType is 1 then we are writing to a file and truncating
                freopen(args[outputIndex], "w", stdout);
            }
            else if (outputType == 2){                  // if outputType is 2 then we are appending to the end of a file
                freopen(args[outputIndex], "a", stdout);
            }

            execlp("ls", "ls", "-al", path, NULL);      // execute the ls command with arguments '-al'
            exit(0);                                    // exit with a status of 0
        }
        else {
            // check if the given argument is a directory.
            if (checkDirectory(args[1]) == 0){
                if (outputType == 1){                   // if outputType is 1 then we are writing to a file and truncating
                    freopen(args[outputIndex], "w", stdout);
                }
                else if (outputType == 2){              // if outputType is 2 then we are appending to the end of a file
                    freopen(args[outputIndex], "a", stdout);
                }
                execlp("ls", "ls", "-al", args[1], NULL);   // execute the ls command with arguments '-al'
            }
            else {
                fprintf(stderr, "%s is not a directory.\n", args[1]); // print to stderr if the directory does not exist
            }
            exit(0);                                    // exit with a status of 0
        }
    }
    else {
        wait(&status);
    }
}

/* Prints out the given arguments back to the user */
void echo(char ** args, int outputType, int outputIndex){
    pid = fork();                                   // create a child process
    if (pid < 0){                                   // if pid returns anything under 0 it fails
        fprintf(stderr, "Error, Unable to fork.\n");
        exit(1);                                    // exit with a status of 1 after fail
    }
    else if (pid == 0){
        if (outputType == 1){                       // if outputType is 1 then we are writing to a file and truncating
            freopen(args[outputIndex], "w", stdout);
        }
        else if (outputType == 2){                  // if outputType is 2 then we are appending to the end of a file
            freopen(args[outputIndex], "a", stdout);
        }
        char finalPrint[MAX_BUFFER];                // create a variable to store the final string
        strcpy(finalPrint, args[1]);                // copy the first string to the the final string
        for (int i = 2; args[i]; i++){              // in each iteration of the loop check if args[i] exists
            if (!strcmp(args[i], ">") || !strcmp(args[i], ">>") || !strcmp(args[i], "<")){
                break;
            }
            strcat(finalPrint, " ");                // add a space before adding the next arg
            strcat(finalPrint, args[i]);            // add the next arg
        }
        execlp("echo", "echo", finalPrint, NULL);   // execute the echo command
        exit(0);                                    // exit with a status of 0
    }
    else {
        wait(&status);
    }
}

/* Stops the shell until the user presses enter */
void pauseShell(){
    printf("Press Enter to continue...\n");
    // using termios.h
    struct termios oldTermAttr;                         // make a struct to hold the current terminal attributes
    struct termios newTermAttr;                         // make another struct that will change the attributes

    tcgetattr(fileno(stdin), &oldTermAttr);             // store the current attributes for stdin in oldTermAttr
    newTermAttr = oldTermAttr;                          // copy over current attributes to newTermAttr
    newTermAttr.c_lflag &= ~ECHO;                       // disable echo in newTermAttr
    tcsetattr(fileno(stdin), TCSANOW, &newTermAttr);    // set the attributes for stdin to the attributes stored in newTermAttr
    // TCSANOW changes the attributes immediately
    char buffer[MAX_BUFFER];                            // variable to store the user input
    fgets(buffer, MAX_BUFFER, stdin);                   // get user input until you get a newline
    tcsetattr(fileno(stdin), TCSANOW, &oldTermAttr);    // reset attributes for stdin back to oldTermAttr
}

/* Executes commands that aren't in the internal commands */
void otherCommands(char * command, char ** args){
    int i = 0, bg = 0;
    while (args[i]){                                    // find the index of the end of the list
        i++;
    }
    // if last arg is '&' then set bg to 1
    if (!strcmp(args[i-1], "&")){
        bg = 1;
    }
    pid = fork();                                       // create a child process
    if (pid < 0){                                       // if pid returns anything under 0 it fails
        fprintf(stderr, "Error, Unable to fork.\n");
        exit(1);
    }
    else if (pid == 0){                                 // if pid is 0, the fork was successful
        char * shellVar;
        shellVar = getenv("shell");                     // store the value of the 'shell' before any executions in shellVar
        setenv("parent", shellVar, 1);                  // set the value for the parent env variable to the shellVar from the parent
        if (bg == 1){                                   // if background execution get rid of the '&' in args
            args[i-1] = NULL;
        }
        execvp(command, args);                          // execute the command, if there are any extra args they will also be ran
        exit(0);
    }
    else {
        if (bg == 0){                                   // if not background execution wait for the exec to exit
            wait(&status);
        }
    }
}

/* Displays the user manual */
void help(char ** args, int outputType, int outputIndex){
    pid = fork();                                               // create a child process
    if (pid < 0){                                               // if pid returns anything under 0 it fails
        fprintf(stderr, "Error, Unable to fork.\n");
        exit(1);
    }
    else if (pid == 0){                                         // if pid is 0, the fork was successful
        if (outputType == 1){                                   // if outputType is 1 then we are writing to a file and truncating
            freopen(args[outputIndex], "w", stdout);
        }
        else if (outputType == 2){                              // if outputType is 2 then we are appending to the end of a file
            freopen(args[outputIndex], "a", stdout);
        }
        chdir(getenv("shellPath"));                             // change the directory for the child to the location of myshell
        execlp("more", "more", "../manual/readme.md", NULL);    // using a path relative to myshell location, open the readme using more
        exit(0);
    }
    else {
        wait(&status);
    }
}