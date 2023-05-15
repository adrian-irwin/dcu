public class Test {
    public static String firstShallBeLast(String word) {
        int length = word.length();
        String swapped = word.substring(length - 1, length) + word.substring(1, length - 1) + word.substring(0, 1);
        // swapped = swapped.concat(word.substring(1, length - 1));
        // swapped = swapped.concat(word.substring(0, 1));
        return swapped;
    }

    public static int largest(int a, int b, int c) {

        int biggest = Integer.max(a, b);
        biggest = Integer.max(biggest, c);
        return biggest;
    }
}
