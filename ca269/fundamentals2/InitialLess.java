import java.util.Scanner;

/*
    Write a program which prompts a user to enter their name and removes their initial and just prints the rest of their name

    Example usage:

    $ java initialLess
    Tell me your name: Jonathan
    Initialless, your name is onathan.
*/
public class InitialLess {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Tell me your name: ");
        String name = in.next();
        in.close();

        String noInitial = name.substring(1);

        System.out.println("Initialless, your name is " + noInitial +".");
    }
}
