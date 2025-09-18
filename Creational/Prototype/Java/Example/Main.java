public class Main {
    public static void main(String[] args) {
        KeyConfig config1 = new KeyConfig("publicKey1", "privateKey1");
        KeyConfig config2 = config1.clone();
        KeyConfig config3 = config1.copyWith(null, "privateKey2");

        System.out.println(config1 == config2);
        System.out.println(config1 == config3);

        System.out.println(config1);
        System.out.println(config2);
        System.out.println(config3);
    }
}