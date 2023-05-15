import java.util.Scanner;

/* Write a program which will read in a positive integer, num, and then, using a while loop, print the numbers from num up to twenty

Here is what the program would do when run.

$ java NumToTwenty
Enter a number: 7
7 8 9 10 11 12 13 14 15 16 17 18 19 20

Note that your output should terminate with a space after the last number and then a newline.
 */
public class NumToTwenty {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = in.nextInt();

        while (num <= 20) {
            System.out.print(num + " ");
            num++;
        }
        System.out.println();
    }
}