import java.util.Scanner;


/*
    Write a program called Temp.java which reads in a temperature in Fahrenheit and converts it to Celsius. However, you should use a method of the Convert class called fahr2cels() which takes a double parameter and returns a double. Use the method as follows:
    Convert.fahr2cels(32)

    You could assign this to a variable called temp with the following assignment statement:
    double temp = Convert.fahr2cels(32);

    Example usage:
    $ java Temp
    Give me a Fahrenheit temperature: 32.0
    In Celsius that would be: 0.0

    Note, this is very short and simple. You do not need to write the Convert class - that is supplied. You just have to use it.
    Also, this exercise just checks the temperature. Any messages that you print will be ignored.
*/
public class Temp {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Give me a Fahrenheit temperature: ");

        double fahr = in.nextDouble();
        in.close();

        double celsius = Convert.fahr2cels(fahr);

        System.out.println("In Celsius that would be: " + celsius);
    }
}
