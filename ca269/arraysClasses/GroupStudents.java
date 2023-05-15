public class GroupStudents {
    public static void main(String [] args) {
        Student [] group = {
            // new Student("John", 50),
            // new Student("Abby", 40),
            // new Student("Dylan", 20),
            // new Student("Carl", 70),
            // new Student("Maeve", 70),
            // new Student("Chris", 44),
            // new Student("James", 55),
            // new Student("Anne", 63),
            // new Student("Johnathon", 39),
            new Student("John", 50),
               new Student("Abby", 40),
               new Student("Dylan", 20),
            };

        Test.print(group);
        System.out.println("-------------------");

        Test.printHonours(group);
        System.out.println("-------------------");

        Test.printForties(group);
        System.out.println("-------------------");

        int numPassed = Test.numberPasses(group);
        System.out.println(numPassed + " students passed out of " + group.length);
        System.out.println("That is an " + 100.0 * numPassed / group.length + "% pass rate.");
        System.out.println("-------------------");

        Student best = Test.getBestStudent(group);
        System.out.println("The best student was " + best.getName() + " with a mark of " + best.getMark());
        System.out.println("-------------------");

        double passingAverage = Test.getPassingAverage(group);
        System.out.println("The average mark of all students who passed is " + passingAverage);
    }
}
