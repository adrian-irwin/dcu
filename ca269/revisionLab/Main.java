import java.util.Scanner;

public class Main {
    public static void main(String [] args){
        String s = "abcdef";
        String newString = Test.firstShallBeLast(s);
        System.out.println("Test.firstShallBeLast(" + s + ") is " + newString);

        // Create a scanner object
        Scanner in = new Scanner(System.in);

        // Read in the three numbers
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        System.out.println("Test.largest(" + a + ", " + b + ", " + c + ") is " + Test.largest(a, b, c));
    }
}
