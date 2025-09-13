public class Main {
    public static void main(String[] args) {
        Computer original = new Computer("Intel i7", "16GB", "512GB SSD");
        System.out.println("Original: " + original);

        Computer cloned = (Computer) original.clone();
        cloned.setCpu("AMD Ryzen 7");
        System.out.println("Cloned: " + cloned);

         // Shallow copy
        Computer shallowCloned = (Computer) original.shallowClone();
        shallowCloned.setCpu("AMD Ryzen 7");
        System.out.println("Shallow Cloned: " + shallowCloned);

        // Deep copy
        Computer deepCloned = (Computer) original.deepClone();
        deepCloned.setCpu("Apple M2");
        System.out.println("Deep Cloned: " + deepCloned);

        // Kiểm tra sự thay đổi của các thuộc tính tham chiếu (nếu có)
        System.out.println("Original after cloning: " + original);
    }
}