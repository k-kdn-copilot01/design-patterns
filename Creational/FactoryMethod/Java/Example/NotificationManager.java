public abstract class NotificationManager {
    public abstract NotificationService createNotificationService();

    public void notify(String destination, String title, String content) {
        NotificationService notificationService = createNotificationService();
        notificationService.notify(destination, title, content);
    }
}
