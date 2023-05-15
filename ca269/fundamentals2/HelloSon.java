import java.util.Scanner;

/*
    Write a program which prompts a user to enter their name and then prints a personalised greeting.

    Example usage:

    $ java HelloSon
    Tell me your name: Jonathan
    Hello Jonathan

*/
public class HelloSon {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Tell me your name: ");
        String name = in.next();
        in.close();
        System.out.println("Hello " + name);
    }
}
