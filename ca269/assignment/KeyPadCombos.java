import java.util.Scanner;

public class KeyPadCombos {
    static String[] keys = {"", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    static int wordCount = 0;


    public static int[] getInputs () {
        Scanner in = new Scanner(System.in);
        System.out.print("\nEnter the numbers that you would like to find all the word combinations for: ");
        String input = in.nextLine();
        int[] numbers = new int[input.length()];
        for (int i = 0; i < input.length(); i++) {
            numbers[i] = Integer.parseInt(input.substring(i, i + 1));
        }
        return numbers;
    }

    public static void findCombos(int[] numbers, String[] output, String temp, int letterIndex) {
        if (letterIndex >= numbers.length) {
            output[wordCount] = temp;
            wordCount++;
            return;
        } else if (numbers[letterIndex] == 1 || numbers[letterIndex] == 0) {
            findCombos(numbers, output, temp, letterIndex + 1);
        }
        String letters = keys[numbers[letterIndex]];
        for (int i = 0; i < letters.length(); i++) {
            temp += letters.charAt(i);
            findCombos(numbers, output, temp, letterIndex + 1);
            temp = temp.substring(0, temp.length() - 1);
        }
    }

    public static int findWordArrayLength(int[] numbers){
        int arrayLength = 1;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] != 1 && numbers[i] != 0) {
                arrayLength *= keys[numbers[i]].length();
            }
        }
        return arrayLength;
    }

    public static String[] makeStringArray(int arrayLength) {
        return new String[arrayLength];
    }

    public static void printWords(String[] words){
        for (int i = 0; i < words.length; i++) {
            System.out.print(words[i] + " ");
        }
    }

    public static void main(String[] args) {
        int[] numbers = getInputs();

        int arrayLength = findWordArrayLength(numbers);

        String[] words = makeStringArray(arrayLength);

        System.out.println("Number of Combinations: " + words.length);

        findCombos(numbers, words, "", 0);
        printWords(words);

        System.out.println("\n");
        wordCount = 0;

        Scanner in = new Scanner(System.in);
        System.out.print("Would you like to find all combinations for other numbers(y/n)?: ");
        String response = in.nextLine();

        if(response.contains("n") || response.contains("N")) {
            System.exit(0);
        }

        while(response.contains("y") || response.contains("Y")) {


            numbers = getInputs();

            arrayLength = findWordArrayLength(numbers);

            words = makeStringArray(arrayLength);

            System.out.println("Number of Combinations: " + words.length);

            findCombos(numbers, words, "", 0);

            printWords(words);

            System.out.println("\n");
            wordCount = 0;

            System.out.print("Would you like to find all combinations for other numbers(y/n)?: ");
            response = in.nextLine();

        }
    }
}
