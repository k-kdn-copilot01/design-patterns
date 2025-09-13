public class Main() {
	public static void main(String[] args) {
		Document document = new Document("Báo cáo", "Nội dung gốc");

		Document document2 = document.clone();
		document2.setContent("Nội dung đã chỉnh sửa");

		System.out.println(document.toString());
		System.out.println(document2.toString());
	}
}