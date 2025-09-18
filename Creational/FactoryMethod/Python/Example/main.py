"""
Main demonstration of the Factory Method pattern with logistics example
"""
from logistics import RoadLogistics, SeaLogistics, AirLogistics
from logistics_manager import LogisticsManager


def main():
    """
    Demonstrate the Factory Method pattern with a real-world logistics scenario
    """
    print("🏭 Factory Method Pattern - Logistics Example")
    print("=" * 60)
    
    # Create different logistics providers
    road_logistics = RoadLogistics()
    sea_logistics = SeaLogistics()
    air_logistics = AirLogistics()
    
    # Scenario 1: Domestic delivery
    print("\n📍 Scenario 1: Domestic Delivery (Short Distance)")
    print("-" * 45)
    LogisticsManager.execute_delivery(road_logistics, "Hanoi to Ho Chi Minh City")
    
    # Scenario 2: International delivery
    print("📍 Scenario 2: International Delivery (Overseas)")
    print("-" * 45)
    LogisticsManager.execute_delivery(sea_logistics, "Vietnam to United States")
    
    # Scenario 3: Express delivery
    print("📍 Scenario 3: Express International Delivery")
    print("-" * 45)
    LogisticsManager.execute_delivery(air_logistics, "Vietnam to Japan")
    
    # Scenario 4: Compare all options
    print("📍 Scenario 4: Logistics Comparison")
    print("-" * 30)
    all_logistics = [road_logistics, sea_logistics, air_logistics]
    LogisticsManager.compare_logistics(all_logistics, "Vietnam to Europe")
    
    print("\n🎉 Factory Method Pattern demonstration completed!")
    print("📝 Notice how each logistics type creates different transport vehicles")
    print("   without the client code knowing the specific implementation details.")


if __name__ == "__main__":
    main()
