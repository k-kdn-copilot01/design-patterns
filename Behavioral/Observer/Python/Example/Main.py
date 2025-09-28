"""
Main - Real-world example of Observer Pattern
News Agency system demonstrating Observer pattern in action
"""

from NewsAgency import NewsAgency
from NewsSubscriber import EmailSubscriber, MobileAppSubscriber, WebsiteSubscriber


def main():
    print("=== Observer Pattern Real-World Example: News Agency System ===\n")
    
    # Create news agency
    print("1. Creating News Agency:")
    cnn = NewsAgency("CNN")
    print(f"   Created: {cnn.get_name()}")
    print(f"   Initial subscribers: {cnn.get_subscriber_count()}\n")
    
    # Create different types of subscribers
    print("2. Creating Subscribers:")
    
    # Email subscribers with specific interests
    email_sub1 = EmailSubscriber("john@email.com", "John Smith", ["Technology", "Sports"])
    email_sub2 = EmailSubscriber("jane@email.com", "Jane Doe", ["Politics", "Business"])
    
    # Mobile app subscribers
    mobile_sub1 = MobileAppSubscriber("device_123", "Alice Johnson", ["Technology", "Entertainment"])
    mobile_sub2 = MobileAppSubscriber("device_456", "Bob Wilson", ["Sports"])
    
    # Website subscribers (no specific interests - get all news)
    website_sub1 = WebsiteSubscriber("https://news-aggregator.com", "News Aggregator")
    website_sub2 = WebsiteSubscriber("https://tech-blog.com", "Tech Blog")
    
    print(f"   Created {6} subscribers with different interests and delivery methods\n")
    
    # Subscribe to news agency
    print("3. Subscribing to News Agency:")
    cnn.subscribe(email_sub1)
    cnn.subscribe(email_sub2)
    cnn.subscribe(mobile_sub1)
    cnn.subscribe(mobile_sub2)
    cnn.subscribe(website_sub1)
    cnn.subscribe(website_sub2)
    print(f"   Total subscribers: {cnn.get_subscriber_count()}\n")
    
    # Publish various news articles
    print("4. Publishing News Articles:")
    
    # Technology news
    cnn.publish_article(
        "New AI Breakthrough in Healthcare",
        "Scientists have developed a new AI system that can diagnose diseases with 99% accuracy...",
        "Technology"
    )
    
    # Sports news
    cnn.publish_article(
        "World Cup Final Results",
        "The championship game ended with an exciting 3-2 victory...",
        "Sports"
    )
    
    # Politics news
    cnn.publish_article(
        "New Policy Announcement",
        "The government announced new economic policies that will affect...",
        "Politics"
    )
    
    # Entertainment news
    cnn.publish_article(
        "Movie Premiere Tonight",
        "The highly anticipated movie will premiere tonight at 8 PM...",
        "Entertainment"
    )
    
    # Business news
    cnn.publish_article(
        "Stock Market Update",
        "The stock market showed significant gains today with tech stocks leading...",
        "Business"
    )
    
    print(f"\n5. Publishing Summary:")
    print(f"   Total articles published: {cnn.get_article_count()}")
    print(f"   Total subscribers: {cnn.get_subscriber_count()}\n")
    
    # Show subscriber statistics
    print("6. Subscriber Statistics:")
    print(f"   📧 {email_sub1.get_name()} ({email_sub1.get_email()}): received {email_sub1.get_received_count()} articles")
    print(f"   📧 {email_sub2.get_name()} ({email_sub2.get_email()}): received {email_sub2.get_received_count()} articles")
    print(f"   📱 {mobile_sub1.get_user_name()} ({mobile_sub1.get_device_id()}): received {mobile_sub1.get_notification_count()} notifications")
    print(f"   📱 {mobile_sub2.get_user_name()} ({mobile_sub2.get_device_id()}): received {mobile_sub2.get_notification_count()} notifications")
    print(f"   🌐 {website_sub1.get_site_name()}: displayed {website_sub1.get_displayed_count()} articles")
    print(f"   🌐 {website_sub2.get_site_name()}: displayed {website_sub2.get_displayed_count()} articles")
    
    # Unsubscribe one subscriber
    print(f"\n7. Unsubscribing One Subscriber:")
    cnn.unsubscribe(email_sub2)
    print(f"   Remaining subscribers: {cnn.get_subscriber_count()}\n")
    
    # Publish one more article to show reduced notifications
    print("8. Publishing Article After Unsubscription:")
    cnn.publish_article(
        "Breaking: Emergency Alert",
        "This is an emergency alert for all subscribers...",
        "Breaking"
    )
    
    print(f"\n9. Final Statistics:")
    print(f"   📧 {email_sub1.get_name()}: received {email_sub1.get_received_count()} articles")
    print(f"   📧 {email_sub2.get_name()}: received {email_sub2.get_received_count()} articles (unsubscribed)")
    print(f"   📱 {mobile_sub1.get_user_name()}: received {mobile_sub1.get_notification_count()} notifications")
    print(f"   📱 {mobile_sub2.get_user_name()}: received {mobile_sub2.get_notification_count()} notifications")
    print(f"   🌐 {website_sub1.get_site_name()}: displayed {website_sub1.get_displayed_count()} articles")
    print(f"   🌐 {website_sub2.get_site_name()}: displayed {website_sub2.get_displayed_count()} articles")
    
    print("\n=== Real-World Example Demo Complete ===")


if __name__ == "__main__":
    main()
