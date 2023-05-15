import java.util.Scanner;

/*
    Write a program which will read in a positive integer, num, from the user and then print the numbers from 1 up to n. Use a while loop appropriately.

    Here is what the program would do when run.
    $ java OneToNum
    Enter a number: 7
    1 2 3 4 5 6 7

    Note that your output should terminate with a space after the last number and then a newline.
*/
public class OneToNum {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = in.nextInt();
        int i = 1;
        while (i <= num) {
            System.out.print(i + " ");
            i++;
        }
        System.out.println();
    }
}
