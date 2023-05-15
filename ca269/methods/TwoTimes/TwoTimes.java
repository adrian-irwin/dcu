import java.util.Scanner;


/*
    Write a program which reads in a integer, n, and prints out n * 2. However, you should not multiply the numbers in your program.
    Instead, use a static method of the Helper class called twoTimes.

    To access this method, provide the name of the class, Helper followed by a dot and the name of the method. The information is passed as a parameter to the method and the result is returned. For example, if you wanted to get 2 times 16, you would call
        Helper.twoTimes(16)

    You could assign this to an integer variable called x with the following assignment statement:
        x = Helper.twoTimes(16);

    Obviously your program would be simpler if you just multiplied by 2, but this is an exercise in using methods. You will get zero marks unless you use the method.

    Example usage:
        $ java TwoTimes
        Enter a number: 4
        Times two is: 8

    Hint: This requires a minor change to the original TwoTimes solution. Find where you calculated twice the number and replace that expression with the method call as indicated above.
    If you spend longer than 5 minutes at this, you are doing it wrong.
*/
public class TwoTimes
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);

        // Ask the user to enter a number
        System.out.print("Enter a number: ");

        int num = in.nextInt();
        in.close();

        // Call the Helper.twoTimes() method to calculate the result
        int result = Helper.twoTimes(num);

        // prepare the user for the result
        System.out.println("Times two is: " + result);
    }
}