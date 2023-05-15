import java.util.Scanner;

/*
    Your program will read in a number, n, and a string, s, and print out the string with the character at position n removed.

    Example
    java ReducedString
    Enter a string: 3 Goodie!
    Gooie!
    Note that counting starts at 0 and so the the character at position 3 is the 'd'. That character has been removed.

    Here is another example:

    java ReducedString
    Enter a string: 0 ABC
    BC
    Position 0 is the first character of the string, the "A" which is removed.

    Yet another example

    java ReducedString
    Enter a string: 1 ABC
    AC
    This time, the second letter (at position 1) is removed.

    Yet another example

    java ReducedString
    Enter a string: 2 ABC
    AB
    This time, the third letter (at position 2) is removed.

    Remember that with the string "ABC" the letter positions are as shown below:

    ABC
    012
    Hint: When you are testing your program, you could use the string "01234567" because then the numbers correspond to the position in the string.
*/
public class ReducedString {
    public static void main(String[] args) {
        // Create a scanner object
        Scanner in = new Scanner(System.in);

        System.out.print("Enter an integer and a string: ");
        // Read in the string
        int position = in.nextInt();
        String word = in.next();
        in.close();
        // work out what to print
        // YOUR CODE HERE

        String part1 = word.substring(0, position);
        String part2 = word.substring(position+1, word.length());

        System.out.println(part1 + part2);
    }
}