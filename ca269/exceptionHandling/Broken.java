public class Broken {
    // method generates an exception
    public void cracked(){
        int [] zap = new int[10];
        System.out.println("Excepting!");
        System.out.println(zap[10]);
    }
}
