/* Create a program which generates an ArrayIndexOutOfBoundsException.

A sample run of your program would look like:

$ java ExceptionMaker
    Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: -1
	at ExceptionMaker.main(ExceptionMaker.java:5)

Your message doesn't have to be the same, you just have to generate an exception. */
public class ExceptionMaker {
    public static void main(String[] args) {
        System.out.println(args[-1]);
    }
}
