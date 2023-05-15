public class Main {
    public static Shape largest(Shape [] shapes)
    {
       if(shapes.length == 0)
          return null;
       Shape largest = shapes[0]; // Assume it's the first
       for(Shape shape : shapes)
          if(shape.area() > largest.area()) // This one is larger ...
             largest = shape;        // ... update the variable

       return largest;
    }

    public static void main(String [] args)
    {
       Rectangle[] rectangles = {
                         new Rectangle("Rectangle",2.0,3.0),
                         new Rectangle("Square",4.0,4.0),
                         };

       Rectangle big = (Rectangle)largest(rectangles);
       System.out.println(big);

       Shape[] shapes = {
                            new Rectangle("Rectangle 1",2.0,3.0),
                            new Rectangle("Rectangle 2",16.0,1.0),
                            new Rectangle("Rectangle 3",7.0,2.0),
                            new Rectangle("Rectangle 4",17.0,1.0),
                            new Circle("Circle 1",1.0),
                            new Circle("Circle 2",2.0),
                            new Circle("Circle 3",3.0),
                            new Circle("Circle 4",4.0),
                            new Rectangle("Rectangle 5",5.0,3.0),
                            new Triangle("Triangle 1",5.0,12.0,13.0),
                            new Rectangle("Square 1",4.0,4.0),
                         };

       System.out.println("The largest shape is: " + largest(shapes));
    }

}
