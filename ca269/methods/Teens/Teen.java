
/*
    Create a class called Teen with one static method called isTeenager.
    This method should take one integer parameter representing an age and return a boolean value, true if the age is that of a teenager and false otherwise.
    Your code could be used as in the following statement:
        System.out.println(Teen.isTeenager(12));
*/
public class Teen {
    public static boolean isTeenager(int age) {
        if (age < 20 && age > 12) {
            return true;
        } else {
            return false;
        }
    }
}
