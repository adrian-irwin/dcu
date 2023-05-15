import java.util.Scanner;

/*
    Write a program which will convert inches to centimetres. The program should ask a user for an inch-eger and convert it to centimeters. You may assume that the user is very ancient and uses an outmoded unit of measurement.

    Note that 1 inch is 2.54 cm

    Example usage:

    $ java inch2cm
    Please enter a quantity in inches: 1
    1 inch is 2.54 cm
    or

    $ java inch2cm
    Please enter a quantity in inches: 2
    2 inch is 5.08 cm
*/
public class Inches2cm {
    public static void main(String[] args) {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        final double oneInchInCm = 2.54;

        // Find out how many inches (use a whole number for integers)
        System.out.print("Please enter a quantity in inches: ");

        int input = in.nextInt();
        in.close();
        double result = input * oneInchInCm;

        // Print out the result
        System.out.println(input + " inch is " + result + " cm");

    }
}
