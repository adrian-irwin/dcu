/* Write a program which will take a set of command line parameters representing integers, total them all up and return the sum of all the integers

A sample run would be:

$ java TotalArgs 5 1 10
    The sum of all the args is 16.

This is tricky, because the arguments start as Strings and you have to convert them to integers if you want to do arithmetic with them. There are a few ways to convert Strings to ints, but the simplest is probably the parseInt method of the Integer class. This can be used as follows:

   String s = "25";
   int num = Integer.parseInt(s);  // This will take the String, s, which is "25" and convert it to the integer 25.
*/
public class TotalArgs {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 0; i < args.length; i++) {
            int num = Integer.parseInt(args[i]);
            sum += num;
        }

        System.out.println("The sum of all the args is " + sum + ".");
    }
}
