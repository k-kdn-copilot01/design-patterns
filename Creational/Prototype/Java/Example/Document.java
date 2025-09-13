public class Document implements Prototype {
    public String title;
    public String content;
    public User author;

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