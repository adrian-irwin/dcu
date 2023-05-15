public class Word {
    public static boolean isFirstLetter(String word, char letter) {
        if (word.charAt(0) == letter) {
            return true;
        }
        return false;
    }

    public static boolean containsLetter(String word, char letter) {
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == letter) {
                return true;
            }
        }
        return false;
    }

    public static boolean allDone(String word, String guesses) {
        int count = 0;
        for (int i = 0; i < word.length(); i++) {
            if (containsLetter(guesses, word.charAt(i))) {
                count++;
            }
        }
        if (count == word.length()) {
            return true;
        }
        return false;
    }

    public static String showLetter(String word, char guess) {
        String result = word;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == guess) {
                result = result.substring(0, i) + guess + result.substring(i+1);
            } else {
                result = result.substring(0, i) + "_" + result.substring(i+1);
            }
        }
        return result;
    }

    public static String showLetters(String word, String guesses) {
        String result = word;

        /* for every letter in word, check every guess and if it is */
        for (int i = 0; i < result.length(); i++) {

            int check = 0;
            char current = '_';

            for (int j = 0; j < guesses.length(); j++) {
                if (result.charAt(i) == guesses.charAt(j)) {
                    check = 1;
                    current = guesses.charAt(j);
                }
            }

            if (check == 1) {
                result = result.substring(0, i) + current + result.substring(i+1);
            } else {
                result = result.substring(0, i) + "_" + result.substring(i+1);
            }

        }

        return result;
    }

    public static void main(String[] args) {
        String word = "baad";
        String guesses = "acdefghijklmnopqrstuvwxyz";
        String abc = "better";
        char def = 'e';
        if (allDone(word, guesses)) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
        System.out.println("----------------------");
        String ghi = "computing";
        String jkl = "gpo";
        System.out.println(showLetters(ghi, jkl));
    }
}