import java.util.Scanner;

public class OnlyHigh {
    public static void main(String[] args) {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.print("Enter a word: ");
        // Read in the word
        String word = in.next();

        for (int i = 0; i < word.length() - 1; i++) {
            String pair = word.substring(i, i+2);
            if (pair.equals("hi")) {
                System.out.println(pair);
            }
        }
    }
}
