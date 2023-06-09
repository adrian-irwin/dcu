/* Examine the following class:

public class Broken
{
   // method generates an exception
   public void cracked()
   {
      int [] zap = new int[10];
      System.out.println("Excepting!");
      System.out.println(zap[10]);
   }
}
This code will generate an Exception as can be seen when the following main method creates an instance of the Broken class and calls the cracked method.

public class Catch
{
   public static void main(String [] args)
   {
      Broken broke = new Broken();

      System.out.println("Testing");
      broke.cracked();
   }
}
When the program is run, the following is printed. Note where the exception occurs.

$ java Catch
Testing
Excepting!
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10
	at Broken.cracked(Broken.java:8)
	at Catch.main(Catch.java:8)
You are to modify the main method so that it catches the exception. When the exception is caught, just print: "Caught the exception."

Sample run:

$ java Catch
Testing
Excepting!
Caught the exception.
$
Note that the cracked() method printed the Excepting! line.

 */
public class Catch {
    public static void main(String[] args) {
        try {
            Broken broke = new Broken();
            System.out.println("Testing");
            broke.cracked();
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught the exception.");
        }
    }
}
