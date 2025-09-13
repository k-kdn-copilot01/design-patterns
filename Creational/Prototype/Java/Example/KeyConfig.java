public class KeyConfig implements Prototype {
    @Override
    public KeyConfig clone() {
        return new KeyConfig(this.publicKey, this.privateKey);
    }

    private String publicKey;
    private String privateKey;

    public KeyConfig(String publicKey, String privateKey) {
        this.publicKey = publicKey;
        this.privateKey = privateKey;
    }

    KeyConfig copyWith(String publicKey, String privateKey) {
        return new KeyConfig(
            publicKey != null ? publicKey : this.publicKey,
            privateKey != null ? privateKey : this.privateKey
        );
    }

    @Override
    public String toString() {
        return "KeyConfig{publicKey='" + publicKey + "', privateKey='" + privateKey + "'}";
    }
}
