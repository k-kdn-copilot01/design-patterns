public class SmsNotificationManager extends NotificationManager {
    @Override
    public NotificationService createNotificationService() {
        return new SmsNotificationService(1000);
    }
}
