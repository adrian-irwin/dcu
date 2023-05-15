import java.util.Scanner;

public class Reverse {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);


        System.out.print("How many numbers: ");
        int num = in.nextInt();

        // Read in the numbers
        int[] numbers = new int[num];
        System.out.print("Enter " + num + " numbers: ");

        // Now read in the numbers
        for (int i = 0; i < num; i++) {
            numbers[i] = in.nextInt();
        }

        // reverse the numbers
        int[] reversed = new int[num];
        for (int j = 0; j < num; j++) {
            reversed[j] = numbers[num - 1 - j];
        }

        System.out.print("The numbers reversed are:");

        // print them out
        for (int k = 0; k < reversed.length; k++) {
            System.out.print(" " + reversed[k]);
        }
        // Use System.out.print(" " + num[i]); and finish with a newline.
        System.out.println();
    }
}
