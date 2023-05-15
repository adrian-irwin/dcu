import java.util.Scanner;

/*
    Write a program which prompts a user to enter their name their age (a whole number) and their favourite colour and prints an appropriate message.

    Example usage:

    $ java TellMeAboutYourself
    Tell me your name: Jonathan
    Jonathan what is your age and your favourite colour: 16 blue
    Hello Jonathan, you are 16 and your favourite colour is blue.
*/
public class TellMeAboutYourself {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Tell me your name: ");
        String name = in.next();

        System.out.print(name + " what is your age and your favourite colour: ");
        int age = in.nextInt();
        String colour = in.next();
        in.close();

        System.out.println("Hello " + name + ", you are " + age + " and your favourite colour is " + colour + ".");
    }
}
