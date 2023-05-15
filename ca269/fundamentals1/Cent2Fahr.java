import java.util.Scanner;

/*
    Your ancient friend is feeling very cold but he doesn't know how cold 'cos he can only see the temperature in degrees Centigrade. He asks you for help because you know all about those new fangled computers.

    Write a program which will convert temperature in degrees Centigrade to temperature in degrees Fahrenheit.

    The temperature T in degrees Fahrenheit (°F) is equal to the temperature T in degrees Celsius (°C) times 9/5 plus 32.

    You should read the centigrade value as a whole number but output the fahrenheit as a floating point number.
*/
public class Cent2Fahr {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Please enter the Temperature in centigrade: ");
        int centigrade = in.nextInt();
        in.close();
        double fahrenheit = ((double) centigrade * 9/5) + 32;

        System.out.println(centigrade + " " + fahrenheit);

    }
}
