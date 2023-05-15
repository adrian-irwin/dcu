import java.util.Scanner;

/*  Write a program which reads in a integer, n, and prints out n squared. Note that n squared is n multiplied by itself.

    Example usage:

    $ java SquareIt
    Enter a number: 4
    4 squared is 16
    Here is another example

    $ java TwoTimes
    Enter a number: 2
    2 squared is 4

    This program is very similar to the last. However you also need to print the number that the user enters.
*/
public class SquareIt {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Ask the user to enter a number
        System.out.print("Enter a number: ");

        // Read in the number (use in.nextInt() and assign it to an integer
        int input = in.nextInt();
        in.close();

        // do the necessary (calculate the result) (Create a variable to hold the result - what type should the variable be?)
        int calculation = input * input;

        // prepare the user for the result
        // print out the result (use System.out.println()
        System.out.println(input + " squared is " + calculation);
    }
}
