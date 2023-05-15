/* Write a program which prints out its command line arguments in reverse order.

A sample run would be:

$ java ReverseArgs Hello 5 58-78-rs
args[2] = 58-78-rs
args[1] = 5
args[0] = Hello

Note that the arguments are printed in reverse order. */
public class ReverseArgs {
    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            System.out.println("args[" + (args.length - i - 1) + "] = " + args[args.length - i - 1]);
        }
    }
}
