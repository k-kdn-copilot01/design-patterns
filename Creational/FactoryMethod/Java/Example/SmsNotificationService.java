public class SmsNotificationService implements NotificationService {
    private final int maxLength;

    public SmsNotificationService(int maxLength) {
        this.maxLength = maxLength;
    }

    @Override
    public void notify(String destination, String title, String content) {
        if (title.length() + content.length() > maxLength) {
            throw new RuntimeException("Title and content too long");
        }
        System.out.printf("Notify by SMS: %s - %s - %s%n", destination, title, content);
    }
}
