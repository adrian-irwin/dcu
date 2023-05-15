import java.util.Scanner;

/* Write a program which will read in a positive integer, num, from the user and then print the numbers from 1 up to n. Your program should use a for loop.

Here is what the program would do when run.

$ java OneToNum
Enter a number: 7
1 2 3 4 5 6 7

Note that your output should terminate with a space after the last number and then a newline.
*/
public class OneToNum {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        in.close();
        for (int i = 1; i <= num; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
