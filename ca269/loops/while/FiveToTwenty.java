
/*
    Write a program which will print out the numbers 5 down to 20 inclusive. Use a while loop.

    Here is what the program would do when run.
    $ java FiveToTwenty
    5 6 7 8 9 11 12 13 14 15 16 17 18 19 20

    Note that your output will finish with a space after the last number and then a newline.
*/
public class FiveToTwenty {
    public static void main(String[] args) {
        int i = 5;
        while (i <= 20) {
            System.out.print(i + " ");
            i++;
        }

        System.out.println();
    }
}
