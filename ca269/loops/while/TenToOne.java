
/*
    Write a program which will print out the numbers 10 down to 1 inclusive. Use a while loop appropriately.

    Here is what the program would do when run.
    $ java TenToOne
    10 9 8 7 6 5 4 3 2 1

    Note that your output will finish with a space after the last number and then a newline.
*/
public class TenToOne {
    public static void main(String[] args) {
        int i = 10;
        while (i >= 1) {
            System.out.print(i + " ");
            i--;
        }

        System.out.println();
    }
}
