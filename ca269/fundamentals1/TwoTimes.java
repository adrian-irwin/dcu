import java.util.Scanner;

/*  Write a program which reads in a integer, n, and prints out n * 2

    Example usage:

    $ java TwoTimes
    Enter a number: 4
    Times two is: 8
    Here is another example

    $ java TwoTimes
    Enter a number: 1
    Times two is: 2
    Your program should create an integer variable. You should create a Scanner class and use the nextInt() method of the Scanner class to get the number from the user. Then use the System.out.println() method to print the result.
*/
public class TwoTimes {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Ask the user to enter a number
        System.out.print("Enter a number: ");

        // Read in the number (use in.nextInt() and assign it to an integer
        int input = in.nextInt();
        in.close();

        // do the necessary (calculate the result) (Create a variable to hold the result - what type should the variable be?)
        int calculation = input * 2;

        // prepare the user for the result
        System.out.print("Times two is: ");
        // print out the result (use System.out.println()
        System.out.println(calculation);
    }
}