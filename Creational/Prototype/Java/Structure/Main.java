public class Main {
    public static void main(String[] args) {
        ClassPrototype original = new ClassPrototype("Intel i7", "16GB");
        System.out.println("Original: " + original);

        ClassPrototype cloned = (ClassPrototype) original.clone();
        cloned.setField1("AMD Ryzen 7");
        System.out.println("Cloned: " + cloned);
    }
}