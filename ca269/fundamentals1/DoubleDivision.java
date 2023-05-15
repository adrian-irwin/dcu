import java.util.Scanner;

/*
    Write a program which will read in two floating point values, a and b, and print out the result of a divided by b.

    Example usage:

    $ java DoubleDivision
    Please enter two floating point numbers: 1.5 0.5
    1.5 / 0.5 is 3.0

    Remember that division by a half is the same as multiplication by two.
*/
public class DoubleDivision {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Please enter two floating point numbers: ");

        double num1 = in.nextDouble();
        double num2 = in.nextDouble();
        in.close();
        double result = num1 / num2;

        System.out.println(num1 + " / " + num2 + " is " + result);

    }
}
