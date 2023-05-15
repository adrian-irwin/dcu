
/*
    Write a program which will print out the numbers 1 to 10 inclusive using a while loop.

    Here is what the program would do when run.
    $ java OneToTen
    1 2 3 4 5 6 7 8 9 10

    Note that your output will finish with a space after the last number and then a newline.
    */
public class OneToTen {
    public static void main(String[] args) {
        int i = 1;
        while(i <= 10) {
            System.out.print(i + " ");
            i++;
        }

        System.out.println();
    }
}