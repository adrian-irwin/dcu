
/*
Name: Adrian Irwin
Student Number: 20415624
I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy,
and any work that is either paraphrased, summarised or directly quoted from the work of others has been referenced.
 */

void printPrompt(char * path);
void checkCommands(char * command, char * path, char ** args, int outputType, int outputIndex);
void clearShell();
int checkDirectory(char * directory);
void changeDirectory(char * path, char ** args);
void printEnviron(char ** envArray, char ** args, int outputType, int outputIndex);
void dir(char * path, char ** args, int outputType, int outputIndex);
void echo(char ** args, int outputType, int outputIndex);
void pauseShell();
void otherCommands(char * command, char ** args);
void help(char ** args, int outputType, int outputIndex);