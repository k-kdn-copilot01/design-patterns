import java.util.List;

public interface FSComponent {
    void ls(String indent);
    default void add(FSComponent c) { throw new UnsupportedOperationException(); }
    default void remove(FSComponent c) { throw new UnsupportedOperationException(); }
    default List<FSComponent> getChildren() { throw new UnsupportedOperationException(); }
}
