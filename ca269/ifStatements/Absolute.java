import java.util.Scanner;

public class Absolute {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = in.nextInt();
        in.close();

        if (number < 0) {
            number = -number;
        }

        System.out.println("The absolute value is " + number + ".");
    }
}
