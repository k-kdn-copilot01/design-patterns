public class EmailNotificationService implements NotificationService {
    @Override
    public void notify(String destination, String title, String content) {
        System.out.printf("Notify by Email: %s - %s - %s%n", destination, title, content);
    }
}
