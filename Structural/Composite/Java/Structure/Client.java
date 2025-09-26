public class Client {
    public static void runStructureDemo() {
        System.out.println("--- Composite Pattern: Structure demo ---");
        // build simple tree
        CompositeNode root = new CompositeNode("root");
        Leaf leaf1 = new Leaf("Leaf 1");
        Leaf leaf2 = new Leaf("Leaf 2");
        root.add(leaf1);

        CompositeNode branch = new CompositeNode("branch");
        branch.add(leaf2);
        branch.add(new Leaf("Leaf 3"));

        root.add(branch);
        root.operation("");

        System.out.println("\nRemove Leaf 2 from branch and print again:");
        branch.remove(leaf2);
        root.operation("");
    }
}
