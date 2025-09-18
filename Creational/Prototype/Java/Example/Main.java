public class Main {
    public static void main(String[] args) {
        User author = new User("GiapNT", 18);
        Document doc1 = new Document("Design pattern", "Kaopiz lesson", author);
        Document doc2 = doc1.clone();

        System.out.println(doc1.author == doc2.author);
    }
}