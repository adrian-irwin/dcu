import java.util.Scanner;

/*
    Write a program which prompts a user to enter their name and tells them how many letters are in their name.

    Example usage:

    $ java LengthOfName
    Tell me your name: Jonathan
    Hello Jonathan, your name has 8 letters.
    You can use the length() method of string to discover its length (which will be the same as the number of letters in the name assuming that the name contains only letters).
*/
public class LengthOfName {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = in.next();
        in.close();

        int lenName = name.length();

        System.out.println("Hello " + name + ", your name has " + lenName + " letters.");

    }
}
