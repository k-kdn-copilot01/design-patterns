"""
Logistics Manager - client code that works with different logistics providers
"""
from logistics import Logistics


class LogisticsManager:
    """
    LogisticsManager - manages different types of logistics operations
    """
    
    @staticmethod
    def execute_delivery(logistics: Logistics, destination: str) -> None:
        """
        Execute delivery using the provided logistics
        
        Args:
            logistics (Logistics): A concrete logistics instance
            destination (str): Delivery destination
        """
        print(f"🚚 Planning delivery to: {destination}")
        print(f"📋 {logistics.plan_delivery()}")
        print("✅ Delivery planned successfully!\n")
    
    @staticmethod
    def compare_logistics(logistics_list: list, destination: str) -> None:
        """
        Compare different logistics options for a destination
        
        Args:
            logistics_list (list): List of logistics providers
            destination (str): Delivery destination
        """
        print(f"🔍 Comparing logistics options for delivery to: {destination}")
        print("=" * 60)
        
        for i, logistics in enumerate(logistics_list, 1):
            logistics_type = logistics.__class__.__name__
            print(f"\nOption {i}: {logistics_type}")
            print("-" * 30)
            transport = logistics.create_transport()
            print(f"📦 {transport.get_capacity()}")
            print(f"🚛 {transport.deliver()}")
        
        print("\n" + "=" * 60)
