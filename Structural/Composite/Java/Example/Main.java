public class Main {
    public static void main(String[] args) {
        System.out.println("--- Composite Pattern: FileSystem Example ---");

        Directory root = new Directory("/");
        Directory home = new Directory("home");
        Directory user = new Directory("user");

        FileLeaf readme = new FileLeaf("README.md", 10);
        FileLeaf notes = new FileLeaf("notes.txt", 5);
        FileLeaf photo = new FileLeaf("photo.jpg", 2048);

        user.add(readme);
        user.add(notes);
        user.add(photo);

        home.add(user);
        root.add(home);

        System.out.println("Initial tree:");
        root.ls("");

        System.out.println("\nAfter removing notes.txt and adding docs folder:");
        user.remove(notes);
        Directory docs = new Directory("docs");
        docs.add(new FileLeaf("spec.pdf", 512));
        user.add(docs);

        root.ls("");
    }
}
