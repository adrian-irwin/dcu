import java.awt.Shape;

public class Average {

    public static double averageArea(ShapeWow [] shapes){
        double sum = 0.0;
        for (ShapeWow shape : shapes) {
            sum += shape.area();
        }
        return sum / shapes.length;
    }
}
