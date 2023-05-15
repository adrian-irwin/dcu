import java.util.Scanner;

/*
    Write a program which reads in three integers and prints out their product. That is, if the three numbers are a, b and c, then the result will be a * b * c

    Example usage:

    $ java Thrice
    Enter three numbers: 2 3 4
    The product is 24
    Here is another example

    $ java Thrice
    Enter three numbers: 2 0 1
    The product is 0

    Note that anything times 0 is zero.
*/
public class Thrice {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Ask the user to enter a number
        System.out.print("Enter three numbers: ");

        // Read in the numbers (you need a variable and an in.nextInt() call for each integer)
        int num1 = in.nextInt();
        int num2 = in.nextInt();
        int num3 = in.nextInt();
        in.close();

        // do the necessary (calculate the result) (Create a variable to hold the result - what type should the variable be?)
        int calculation = num1 * num2 * num3;

        // prepare the user for the result
        // print out the result (use System.out.println() )
        System.out.println("The product is " + calculation);
    }
}
