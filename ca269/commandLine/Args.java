/* Write a program which prints out its command line arguments, one argument per line.

A sample run would be:

$ java Args Hello 5 58-78-rs
    args[0] = Hello
    args[1] = 5
    args[2] = 58-78-rs

In this case, there are three arguments: "Hello", "5" and "58-78-rs". Your program should print each argument as shown above. You should create a class called Args in a file called Args.java */
public class Args {
    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            System.out.println("args[" + i + "] = " + args[i]);
            // System.out.printf("args[%d] = %s\n", i, args[i]);
        }
    }
}
