public class FileLeaf implements FSComponent {
    private String name;
    private int sizeKB;

    public FileLeaf(String name, int sizeKB) { this.name = name; this.sizeKB = sizeKB; }

    @Override
    public void ls(String indent) {
        System.out.println(indent + "- File: " + name + " (" + sizeKB + " KB)");
    }
}
