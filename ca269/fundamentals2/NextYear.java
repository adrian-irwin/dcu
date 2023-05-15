import java.util.Scanner;

/*
    Write a program which prompts a user to enter their name their age (a whole number) and tells them how old they will be next year.

    Example usage:

    $ java NextYear
    What is your name: Jonathan
    What age are you: 16
    Hello Jonathan, next year you will be 17.
*/
public class NextYear {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("What is your name: ");
        String name = in.next();

        System.out.print("What age are you: ");
        int age = in.nextInt() + 1;
        in.close();

        System.out.println("Hello " + name + ", next year you will be " + age + ".");

    }
}
