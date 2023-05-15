
/* Write a program which will print out the numbers 1 to 10 inclusive using a for loop.

Here is what the program would do when run.

$ java OneToTen
1 2 3 4 5 6 7 8 9 10

Note that your output should terminate with a space after the last number and then a newline.
*/
public class OneToTen {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
