import java.util.Scanner;

public class SplitWord {
    public static void main(String[] args) {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.print("Enter a word: ");
        // Read in the word
        String word = in.next();

        for (int i = 0; i < word.length() - 1; i++) {
            System.out.println(word.charAt(i) + "" + word.charAt(i+1));
        }
    }
}
