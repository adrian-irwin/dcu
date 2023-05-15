public class Circle extends Shape {

    private double radius;

    public Circle(String n, double r){
        super(n);
        radius = r;
    }

    double area(){
        return Math.PI * radius * radius;
    }
}
