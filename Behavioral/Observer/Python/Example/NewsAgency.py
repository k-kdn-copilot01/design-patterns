"""
NewsAgency - Real-world example of Observer pattern
Represents a news agency that publishes news articles
"""

from typing import List, Dict, Any
import datetime


class NewsSubscriber:
    """Abstract interface for news subscribers"""
    
    def update(self, news_agency, article: Dict[str, Any]) -> None:
        """Called when new article is published"""
        pass


class NewsAgency:
    """News Agency that publishes articles and notifies subscribers"""
    
    def __init__(self, name: str):
        self._name = name
        self._subscribers: List[NewsSubscriber] = []
        self._articles: List[Dict[str, Any]] = []
    
    def subscribe(self, subscriber: NewsSubscriber) -> None:
        """Subscribe to news updates"""
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
            print(f"New subscriber added to {self._name}. Total subscribers: {len(self._subscribers)}")
    
    def unsubscribe(self, subscriber: NewsSubscriber) -> None:
        """Unsubscribe from news updates"""
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
            print(f"Subscriber removed from {self._name}. Total subscribers: {len(self._subscribers)}")
    
    def publish_article(self, title: str, content: str, category: str) -> None:
        """Publish a new article and notify all subscribers"""
        article = {
            'id': len(self._articles) + 1,
            'title': title,
            'content': content,
            'category': category,
            'published_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'agency': self._name
        }
        
        self._articles.append(article)
        print(f"\n📰 {self._name} published: '{title}'")
        print(f"   Category: {category}")
        print(f"   Published at: {article['published_at']}")
        
        # Notify all subscribers
        self._notify_subscribers(article)
    
    def _notify_subscribers(self, article: Dict[str, Any]) -> None:
        """Notify all subscribers about new article"""
        print(f"   📢 Notifying {len(self._subscribers)} subscribers...")
        for subscriber in self._subscribers:
            subscriber.update(self, article)
    
    def get_article_count(self) -> int:
        """Get total number of published articles"""
        return len(self._articles)
    
    def get_subscriber_count(self) -> int:
        """Get total number of subscribers"""
        return len(self._subscribers)
    
    def get_name(self) -> str:
        """Get agency name"""
        return self._name
