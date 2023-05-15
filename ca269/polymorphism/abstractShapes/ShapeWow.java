public abstract class ShapeWow{
    private String name;

    public ShapeWow(String name)
    {
        this.name = name;
    }

    abstract double area();

    public String toString()
    {
        return name + " with area " + area();
    }
}