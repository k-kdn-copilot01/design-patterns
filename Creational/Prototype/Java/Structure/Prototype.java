public interface Prototype{
    Prototype clone()
}
public class ClassPrototype implements Prototype {
    private String field1;
    private String field2;

    public ClassPrototype(String field1, String field2) {
        this.field1 = field1;
        this.field2 = field2;
    }


    public void setField1(String field1) {
        this.field1 = field1;
    }
    @Override
    public Prototype clone() {
        return new ClassPrototype(this.field1, this.field2);
    }

    @Override
    public String toString() {
        return "ClassPrototype [field1=" + field1 + ", field2=" + field2 + "]";
    }
}