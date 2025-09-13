/**
 * Document represents a prototype for cloning documents
 * with various properties and content
 */
public class Document implements Prototype {
    private String title;
    private String content;
    private String author;
    private java.util.List<String> tags;
    private DocumentMetadata metadata;
    
    public Document(String title, String content, String author) {
        this.title = title;
        this.content = content;
        this.author = author;
        this.tags = new java.util.ArrayList<>();
        this.metadata = new DocumentMetadata();
        System.out.println("Document created: " + title);
    }
    
    // Private constructor for cloning
    private Document(Document other) {
        this.title = other.title + " (Copy)";
        this.content = other.content;
        this.author = other.author;
        this.tags = new java.util.ArrayList<>(other.tags); // Deep copy of list
        this.metadata = other.metadata.clone(); // Deep copy of metadata
        System.out.println("Document cloned: " + this.title);
    }
    
    @Override
    public Prototype clone() {
        return new Document(this);
    }
    
    @Override
    public String getInfo() {
        return String.format("Document[title='%s', author='%s', tags=%s, %s]", 
                           title, author, tags, metadata.getInfo());
    }
    
    public void addTag(String tag) {
        tags.add(tag);
    }
    
    public void setContent(String content) {
        this.content = content;
        metadata.incrementVersion();
    }
    
    public String getTitle() {
        return title;
    }
    
    public String getContent() {
        return content;
    }
    
    public java.util.List<String> getTags() {
        return tags;
    }
    
    public DocumentMetadata getMetadata() {
        return metadata;
    }
}