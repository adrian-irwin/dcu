import java.util.Scanner;

public class SquareIt {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Ask the user to enter a number
        System.out.print("Enter a number: ");

        // Read in the number
        int num = in.nextInt();
        in.close();

        // call the square method of the Helper class to get num squared.
        int result = Numbers.square(num);

        System.out.println(num + " squared is " + result);

    }
}
