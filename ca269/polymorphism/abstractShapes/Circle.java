public class Circle extends ShapeWow {

    private double radius;

    public Circle(String n, double r){
        super(n);
        radius = r;
    }

    double area(){
        return Math.PI * radius * radius;
    }
}
