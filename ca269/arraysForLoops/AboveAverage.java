import java.util.Scanner;

public class AboveAverage {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("How many numbers: ");
        int num = in.nextInt();

        // Create an array
        double[] numbers = new double[num];

        System.out.print("Enter " + num + " numbers: ");

        // Now read in the numbers

        double average = 0;
        double currentNum;
        for (int i = 0; i < num; i++) {
            currentNum = in.nextDouble();
            numbers[i] = currentNum;
            average += currentNum;
        }
        average /= num;


        // double average = sum / num;
        System.out.println("The average is " + average);

        // Print out the numbers greater than the average
        System.out.print("The above average numbers are:");

        for (int j = 0; j < numbers.length; j++) {
            if (numbers[j] > average) {
                // System.out.println(numbers[j]);
                System.out.print(" " + numbers[j]); // You may want to put this in a loop.
            }
        }

        System.out.println(); // Should finish with a new line
    }
}
