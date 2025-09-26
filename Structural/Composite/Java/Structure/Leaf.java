public class Leaf implements Component {
    private String name;

    public Leaf(String name) { this.name = name; }

    @Override
    public void operation(String indent) {
        System.out.println(indent + "- Leaf: " + name);
    }
}
