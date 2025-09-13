public class Document implements Prototype {
    private String title;
    private String content;
    private User author;

    public Document(String title, String content, User author) {
        this.title = title;
        this.content = content;
        this.author = author;
    }

    @Override
    public Document clone() {
        User author_clone = author.clone();
        return new Document(this.title, this.content, author_clone);
    }
}