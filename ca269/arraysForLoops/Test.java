public class Test {
    public static int getSum(int[] numbers) {
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }
        return sum;
    }

    public static int countFives(int[] numbers) {
        int fives = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == 5) {
                fives++;
            }
        }
        return fives;
    }

    public static int countEven(int[] numbers) {
        int evens = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 == 0) {
                evens++;
            }
        }
        return evens;
    }
    public static void main(String[] args) {
        int[] num = {2, 3, 5, 4, 11, 13, 10, 5, 10, -5, 5};
        System.out.println(countEven(num));
    }
}
