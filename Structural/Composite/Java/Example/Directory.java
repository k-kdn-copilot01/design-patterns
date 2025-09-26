import java.util.ArrayList;
import java.util.List;

public class Directory implements FSComponent {
    private String name;
    private List<FSComponent> children = new ArrayList<>();

    public Directory(String name) { this.name = name; }

    @Override
    public void ls(String indent) {
        System.out.println(indent + "+ Dir: " + name);
        for (FSComponent c : children) c.ls(indent + "  ");
    }

    @Override
    public void add(FSComponent c) { children.add(c); }

    @Override
    public void remove(FSComponent c) { children.remove(c); }

    @Override
    public List<FSComponent> getChildren() { return children; }
}
