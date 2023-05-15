import java.util.Scanner;

/*
Write a program which will keep reading in numbers until it comes to a -1. Your program should then print the number which was just before the -1.

Here is what the program would do when run.

$ java NoMinusOne
Enter numbers: 30 15 4 -6 9 -1
The penultimate number was: 9

$ java NoMinusOne
Enter numbers: 5 100 -1
The penultimate number was: 100
*/
public class NoMinusOne {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter numbers: ");
        int i = in.nextInt();
        int penultimate = 0;
        for (; i != -1; i = in.nextInt()) {
            penultimate = i;
        }
        System.out.println("The penultimate number was: " + penultimate);
    }
}
