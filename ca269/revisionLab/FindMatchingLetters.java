import java.util.Scanner;

public class FindMatchingLetters
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.println("Enter two lines:");
        // Read in the two lines
        String line1 = in.nextLine();
        String line2 = in.nextLine();

        int numMatching = 0;
        for (int i = 0; i < line1.length(); i++) {
            if (line1.substring(i, i+1).equals(line2.substring(i, i+1))) {
                numMatching++;
            }
        }
        // it should work out what the number of matching characters is

        // Print out the solution
        System.out.println("There are " + numMatching + " corresponding characters.");
    }
}