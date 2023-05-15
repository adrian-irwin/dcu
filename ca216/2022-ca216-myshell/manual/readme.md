
Description  
    myshell is a command interpreter, or shell, that has 8 defined internal commands and has support for other commands that are not included in the internal commands.  
    myshell also supports I/O redirection, batchmode and background execution.  
  
Definitions  
    The following are definitions for terms that are used in this help document.  
  
    'environment variable'  
        Environment variables are dynamic named variables stored in the shell that are accessible to all commands in the shell. [1]  
        These variables make it easier for commands to access information about the shell.  
  
    'fork'  
        fork is a system call that creates a new child process which is a duplicate of the process that called it. [2]  
        These duplicate processes are used to execute commands separetly from the main process.  
  
Running Commands  
    Commands are run by inputting the name of the command, then on a case by case basis there will be some arguments for the commands.  
    Both internal and other commands consist of the command name itself, then it's arguments, and all of this is separated either by spaces or tabs. [3]  
        e.g. echo Hello World,  
            'echo' is the command name, and 'Hello' and 'World' are the arguments  
  
Internal Commands  
    cd {directory}  
        Changes the current directory that the shell is in to {directory}.  
        If no {directory} is given then we print the current directory that the user is in.  
        If the given {directory} does not exist an error is printed.  
    clr  
        Clears the shell screen and brings the command prompt to the top of the screen  
    dir {directory}  
        Lists the contents of the current directory if there is no given {directory}.  
        If there is a given directory, dir lists the content for the given {directory}.  
        If the given {directory} is not a directory dir will return '{directory} is not a directory.'  
    environ  
        Lists all of the shell's environment variables and their values.  
    echo {arg1, arg2 ...}  
        Prints all given arguments back to the user.  
    help  
        Prints out this help manual.  
        It can be scrolled through in two ways:  
            space - scrolls down by the amount of lines that can be displayed on your screen  
            enter - scrolls down line by line  
    pause  
        Stops shell operation until the user presses 'Enter'.  
    quit  
        Quits the shell.  
        Can also be ran by entering 'exit'.  
  
Other Commands  
    If a user inputs a command that is not in the list of defined commands, the shell will pass it onto the system in a child process using fork and try to run the command in the forked process.  
    For example 'ls' is not an internal command but the shell would still attempt to execute this command.  
  
Batchmode  
    Batchmode is a way of invoking shell commands from the command line using a file that contains commands separated by new lines.  
    If there is an argument when invoking the shell then it is assumed that this argument is a file containing commands to be executed by the shell.  
    The shell will try to run these commands then the shell will quit.  
    e.g. ./myshell commands.txt  
        commands.txt includes the below lines:  
            cd  
            environ  
            dir  
        The shell execute these commands line by line, print the outputs of them to the shell and quit after printing the output of dir.  
  
I/O Redirection  
    I/O (Input/Output) redirection is the process of either redirecting input from a file with commands to the shell or redirecting output from commands executed in the shell to a file. [4]  
    This is achieved with the '<', '>' and '>>' operators. [4]  
  
    Input Redirection  
        Input redirection is similar to batchmode but can be done from within the shell  
        It can be achieved by adding a '<' followed by a filename as arguments in the shell,  
        input will be changed to the contents of the file.  
        At the end of the file the shell will quit.  
        e.g. < commands.txt  
            In this example commands.txt has the lines below in the file:  
                echo Hello World  
                dir  
                environ  
            The shell would recognise the '<' and take standard input from commands.txt and run the commands in the file line by line.  
  
    Output Redirection  
        Output Redirection takes the output of commands and either writes or appends it to a file.  
        It is achieved by adding either a '>' or '>>' followed by a filename as arguments in the shell.  
        If the filename provided does not exist the file will be created.  
  
        Writing  
            The contents of the file will be erased and replaced with the output from the shell.  
            Writing output to a file is done by adding '>' with a filename as arguments in the shell.  
            e.g. echo Hello World > output.txt  
                If 'output.txt' didn't exist the file would be created in the current working directory.  
                The output of 'echo Hello World' will be printed to the file 'output.txt' instead of being printed back to the shell.  
                output.txt would have the line below in the file:  
                    Hello World  
  
        Appending  
            Output from the shell will be added onto the end of the file.  
            Appending to a file is done by using '>>' with a filename as arguments in the shell.  
            e.g. echo Hello Again >> output.txt  
                In this example we are redirecting to the same file used in the Writing example.  
                The output of 'echo Hello Again' would be added onto the file 'output.txt'.  
                output.txt would then have the below lines:  
                    Hello World  
                    Hello Again  
  
Background Execution  
    Background execution is when a command is ran in the background giving the user the ability to run other commands in the foreground as the background command is executed.  
    To invoke background execution the user has to have '&' as the last argument when running a command.  
    Background execution is only implemented for other commands.  
        e.g. sleep 5 &,  
            Running this command without '&' we would have to wait for 5 seconds while the system pauses before we can run any code in our shell.  
            By adding '&' as an argument the system pauses for 5 seconds in the background and we are still able to run commands in the shell.  
  
  
References:  
[1] J. Wallen, “Linux 101: What are environment variables?”, TechRepublic, https://www.techrepublic.com/article/linux-101-what-are-environment-variables/ (accessed Mar. 10 2022).  
  
[2] "fork(2): create child process", Linux Programmer's Manual, https://linux.die.net/man/2/fork (accessed Mar. 10 2022).  
  
[3] "Bash Reference Manual", GNU, https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Commands (accessed Mar. 10 2022).  
  
[4] A. Kili, “Learn The Basics of How Linux I/O (Input/Output) Redirection Works”, TecMint, https://www.tecmint.com/linux-io-input-output-redirection-operators/ (accessed Mar. 8 2022).  
  
  
Name: Adrian Irwin  
Student Number: 20415624  
I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy,  
and any work that is either paraphrased, summarised or directly quoted from the work of others has been referenced.  

