import java.util.Scanner;

public class Main
{
    public static Animal [] makeSomeNoise()
    {
        Animal [] animals = {new Cat("Angel"), new Cat("Cheesire"), new Dog("Buster"), new Dog("Fido"), new Cat("Lassie")};
        return animals;
    }

    public static void main(String [] args)
    {
        Animal [] animals = makeSomeNoise();
        for(Animal animal : animals)
            System.out.println(animal.greeting());
    }
}
