import java.util.Scanner;

/*
    Write a program which prompts a user to enter their name and and produces a nickname formed from the their first three letters of their name. You may assume that there are at least three letters in the name.

    Example usage:

    $ java FirstThree
    Tell me your name: Jonathan
    Your nickname is Jon.
    You can use the substring() method of string to get the nickname. You need to think about the parameters you choose.
*/
public class FirstThree {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Tell me your name: ");
        String name = in.next();
        in.close();

        String nickname = name.substring(0,3);

        System.out.println("Your nickname is " + nickname + ".");

    }
}
