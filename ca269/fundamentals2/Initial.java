import java.util.Scanner;

/*
    Write a program which prompts a user to enter their name and gives them their first initial.

    Example usage:

    $ java Initial
    Tell me your name: Jonathan
    Jonathan starts with the letter J.
    You can use the substring() method of string to discover the first letter of the string. You need to think about the parameters you choose.
*/
public class Initial {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = in.next();
        in.close();

        String letter = name.substring(0,1);

        System.out.println(name + " starts with the letter " + letter + ".");

    }
}
