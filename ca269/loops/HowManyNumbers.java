import java.util.Scanner;

/* Write a program which will keep reading in numbers until it comes to a -1. Your program should then print how many numbers were entered (don't include the -1).

Here is what the program would do when run.

$ java HowManyNumbers
Enter numbers: 30 15 4 -6 9 -1
5 numbers were entered.


$ java HowManyNumbers
Enter numbers: 5 100 -1
2 numbers were entered.
*/
public class HowManyNumbers {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter numbers: ");
        int i = in.nextInt();
        int count = 0;
        for (; i != -1; i = in.nextInt()) {
            count++;
        }
        System.out.println(count + " numbers were entered.");
    }
}
