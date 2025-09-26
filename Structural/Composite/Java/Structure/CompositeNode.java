import java.util.ArrayList;
import java.util.List;

public class CompositeNode implements Component {
    private String name;
    private List<Component> children = new ArrayList<>();

    public CompositeNode(String name) { this.name = name; }

    @Override
    public void operation(String indent) {
        System.out.println(indent + "+ Composite: " + name);
        for (Component c : children) {
            c.operation(indent + "  ");
        }
    }

    @Override
    public void add(Component c) { children.add(c); }

    @Override
    public void remove(Component c) { children.remove(c); }

    @Override
    public List<Component> getChildren() { return children; }
}
