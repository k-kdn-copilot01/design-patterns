public class Document implements Prototype {
	private String title;
	private String content;

	public Document(String title, String content) {
		this.title = title;
		this.content = content;
	}

	@Override
	public toString() {
		return "Document [title=" + title + ", content=" + content + "]";
	}

	public void setContent(String content) {
		this.content = content;
	}

	@Override
	public Prototype clone() {
		return new Document(this.title, this.content);
	}
}