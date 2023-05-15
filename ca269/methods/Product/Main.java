import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Ask the user to enter a number
        System.out.print("Enter two numbers: ");

        // Read in the number
        int a = in.nextInt();
        int b = in.nextInt();
        in.close();
        
        // call the multiply method of the Product class.
        int result = Product.multiply(a, b);

        System.out.println(a + " times " + b + " is " + result);
    }
}
