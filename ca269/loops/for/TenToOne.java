
/* Write a program which will print out the numbers 10 down to 1 inclusive using a for loop.

Here is what the program would do when run.

$ java TenToOne
10 9 8 7 6 5 4 3 2 1

Note that your output should terminate with a space after the last number and then a newline.
*/
public class TenToOne {
    public static void main(String[] args) {
        for (int i = 10; i >= 1; i--) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
