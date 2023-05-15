import java.util.Scanner;

public class HiCounter{
    public static void main(String[] args) {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.print("Enter a phrase: ");
        // Read in the phrase (actually the whole line)
        String phrase = in.nextLine();

        // count how many times "hi" occurs.
        int count = 0;
        for (int i = 0; i < phrase.length() - 1; i++) {
            String pair = phrase.substring(i, i+2);
            if (pair.equals("hi")) {
                count++;
            }
        }
        System.out.println(count);
    }
}
