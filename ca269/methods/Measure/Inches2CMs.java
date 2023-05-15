import java.util.Scanner;

public class Inches2CMs {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Ask the user to enter a number
        System.out.print("Enter a number: ");

        // Read in the number
        double num = in.nextDouble();
        in.close();

        double result = Measure.inches2CMs(num);

        System.out.println(num + " inches is " + result + " CMs.");

    }
}
