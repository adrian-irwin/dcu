import java.util.Scanner;

/*
    Write a program which reads in two integers and prints out their sum

    Example usage:

    $ java SumIt
    Enter two numbers: 4 6
    4 and 6 is 10
    Here is another example

    $ java SumIt
    Enter two numbers: 2 0
    2 and 0 is 2
*/
public class SumIt {
    public static void main(String [] args) {
        Scanner in = new Scanner(System.in);

        // Ask the user to enter a number
        System.out.print("Enter two numbers: ");

        // Read in the numbers (you need a nextInt for each integer)
        int num1 = in.nextInt();
        int num2 = in.nextInt();
        in.close();

        // do the necessary (calculate the result) (Create a variable to hold the result - what type should the variable be?)
        int calculation = num1 + num2;

        // prepare the user for the result
        // print out the result (use System.out.println() )
        System.out.println(num1 + " and " + num2 + " is " + calculation);

    }
}