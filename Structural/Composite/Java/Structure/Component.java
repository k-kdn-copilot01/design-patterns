import java.util.List;

public interface Component {
    void operation(String indent);
    // optional: composite management (default unsupported)
    default void add(Component c) { throw new UnsupportedOperationException(); }
    default void remove(Component c) { throw new UnsupportedOperationException(); }
    default List<Component> getChildren() { throw new UnsupportedOperationException(); }
}
