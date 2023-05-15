
/* Write a program which will print out the numbers 5 down to 20 inclusive using a for loop.

$ java FiveToTwenty
5 6 7 8 9 11 12 13 14 15 16 17 18 19 20

Note that your output should terminate with a space after the last number and then a newline.
*/
public class FiveToTwenty {
    public static void main(String[] args) {
        for (int i = 5; i <= 20; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
