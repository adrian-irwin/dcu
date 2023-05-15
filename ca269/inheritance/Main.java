import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Parent parent = new Child();
        System.out.println("parent.makeATwo() is " + parent.makeATwo());
        Animal pig = new Pig("yo");

        System.out.println(pig.greeting());

        Scanner in = new Scanner(System.in);

        String name = in.nextLine();

        Animal ani = new Animal(name);
        System.out.println(ani.greeting());
    }
}
