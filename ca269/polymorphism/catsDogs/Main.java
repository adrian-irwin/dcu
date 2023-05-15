public class Main {
    public static void main(String[] args) {
        Animal cat = new Cat("Angel");
        Animal dog = new Dog("Fido");
        System.out.println(cat.greeting());
        System.out.println(dog.greeting());

    }
}
