public class EmailNotificationManager extends NotificationManager {
    @Override
    public NotificationService createNotificationService() {
        return new EmailNotificationService();
    }
}
