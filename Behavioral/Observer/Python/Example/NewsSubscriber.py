"""
NewsSubscriber - Real-world example of Observer pattern
Different types of news subscribers with specific interests
"""

from NewsAgency import NewsSubscriber, NewsAgency
from typing import List, Dict, Any


class EmailSubscriber(NewsSubscriber):
    """Email subscriber that receives news via email"""
    
    def __init__(self, email: str, name: str, interests: List[str] = None):
        self._email = email
        self._name = name
        self._interests = interests or []
        self._received_articles: List[Dict[str, Any]] = []
    
    def update(self, news_agency: NewsAgency, article: Dict[str, Any]) -> None:
        """Receive news update via email"""
        # Check if subscriber is interested in this category
        if self._interests and article['category'] not in self._interests:
            return
        
        self._received_articles.append(article)
        print(f"   📧 Email sent to {self._email} ({self._name}): '{article['title']}'")
    
    def get_email(self) -> str:
        """Get subscriber email"""
        return self._email
    
    def get_name(self) -> str:
        """Get subscriber name"""
        return self._name
    
    def get_received_count(self) -> int:
        """Get number of articles received"""
        return len(self._received_articles)


class MobileAppSubscriber(NewsSubscriber):
    """Mobile app subscriber that receives push notifications"""
    
    def __init__(self, device_id: str, user_name: str, interests: List[str] = None):
        self._device_id = device_id
        self._user_name = user_name
        self._interests = interests or []
        self._notifications: List[Dict[str, Any]] = []
    
    def update(self, news_agency: NewsAgency, article: Dict[str, Any]) -> None:
        """Receive news update via push notification"""
        # Check if subscriber is interested in this category
        if self._interests and article['category'] not in self._interests:
            return
        
        self._notifications.append(article)
        print(f"   📱 Push notification sent to {self._device_id} ({self._user_name}): '{article['title']}'")
    
    def get_device_id(self) -> str:
        """Get device ID"""
        return self._device_id
    
    def get_user_name(self) -> str:
        """Get user name"""
        return self._user_name
    
    def get_notification_count(self) -> int:
        """Get number of notifications received"""
        return len(self._notifications)


class WebsiteSubscriber(NewsSubscriber):
    """Website subscriber that displays news on website"""
    
    def __init__(self, website_url: str, site_name: str):
        self._website_url = website_url
        self._site_name = site_name
        self._displayed_articles: List[Dict[str, Any]] = []
    
    def update(self, news_agency: NewsAgency, article: Dict[str, Any]) -> None:
        """Display news on website"""
        self._displayed_articles.append(article)
        print(f"   🌐 News displayed on {self._site_name} ({self._website_url}): '{article['title']}'")
    
    def get_website_url(self) -> str:
        """Get website URL"""
        return self._website_url
    
    def get_site_name(self) -> str:
        """Get site name"""
        return self._site_name
    
    def get_displayed_count(self) -> int:
        """Get number of articles displayed"""
        return len(self._displayed_articles)
