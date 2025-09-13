/**
 * DocumentMetadata class to demonstrate deep cloning of nested objects
 */
public class DocumentMetadata {
    private java.time.LocalDateTime createdAt;
    private java.time.LocalDateTime lastModified;
    private int version;
    private String status;
    
    public DocumentMetadata() {
        this.createdAt = java.time.LocalDateTime.now();
        this.lastModified = java.time.LocalDateTime.now();
        this.version = 1;
        this.status = "Draft";
    }
    
    // Copy constructor for cloning
    private DocumentMetadata(DocumentMetadata other) {
        this.createdAt = other.createdAt; // LocalDateTime is immutable, safe to copy reference
        this.lastModified = java.time.LocalDateTime.now(); // Set new modification time for clone
        this.version = 1; // Reset version for clone
        this.status = other.status;
    }
    
    public DocumentMetadata clone() {
        return new DocumentMetadata(this);
    }
    
    public void incrementVersion() {
        this.version++;
        this.lastModified = java.time.LocalDateTime.now();
    }
    
    public void setStatus(String status) {
        this.status = status;
        this.lastModified = java.time.LocalDateTime.now();
    }
    
    public String getInfo() {
        return String.format("Metadata[version=%d, status='%s', created=%s]", 
                           version, status, createdAt.toString().substring(0, 19));
    }
    
    public int getVersion() {
        return version;
    }
    
    public String getStatus() {
        return status;
    }
}