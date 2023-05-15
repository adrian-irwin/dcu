import java.util.Scanner;

/*
    Write a program which prompts a user to enter their name and and tells the user the last letter in their name.

    Example usage:

    $ java LastLetter
    What is your name: Jonathan
    The last letter in your name is n.
    This is a little tricky. You need to use the length() method along with the substring method. In addition, remember that the index of the last letter is one less than the length.
*/
public class LastLetter {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("What is your name: ");
        String name = in.next();
        in.close();

        int lenName = name.length();
        String lastLetter = name.substring(lenName - 1);

        System.out.println("The last letter of your name is " + lastLetter + ".");

    }
}
