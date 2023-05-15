#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

extern int errno;        // system error number
void syserr(char* msg);     // error report and abort routine
void pidyolk();

int main(int argc, char *argv[])
{
   pid_t pid;            // process ID
//    int rc;               // return code
// pid_t test;

   pid = getpid();       // get our own pid
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

    pid = fork();
    if (pid < 0){
        /* error occurred */
        syserr("fork");
    }
    else if (pid == 0){
        /* child process */
        pid = getpid();

        printf("I am the child %d\n", pid);
        execlp("/bin/ls", "ls", NULL);
        return 0;
    }
    else
    {
        /* code */
   pid = getpid();        // reget our pid
   printf("Process ID in parent after fork: %d\n", pid);
    }


        /* parent process */
        /* parent will wait for the child to complete */
        // printf("I am the parent %d\n", pid);

        // cpid = wait(&status);

        // printf("Child Complete (pid=%d) with status=%d\n", cpid, status);




// continued execution in parent process

   pid = getpid();        // reget our pid
   printf("Process ID in parent after fork: %d\n", pid);
    pidyolk();
   exit(0);
}

void syserr(char * msg)   // report error code and abort
{
   fprintf(stderr,"%s: %s", strerror(errno), msg);
   abort();
}

void pidyolk(){
    pid_t asdfasf;
    asdfasf = getpid();        // reget our pid
   printf("Process ID in dasfasdfasdfsadf: %d\n", asdfasf);
}