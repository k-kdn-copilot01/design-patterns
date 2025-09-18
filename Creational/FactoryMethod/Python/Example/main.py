"""
Main demonstration of Factory Method pattern with real-world logistics example.

This script demonstrates the Factory Method pattern using a practical logistics
system where different logistics companies can create different types of transport
methods (trucks, ships) through the same factory method interface.
"""

from concrete_logistics import RoadLogistics, SeaLogistics


def client_code(logistics_company, cargo: str, destination: str, distance_km: float):
    """
    Client code that works with any logistics company through the base Logistics interface.
    
    The client code doesn't need to know the specific logistics company or transport type.
    It works with logistics companies and transports through their abstract interfaces.
    
    Args:
        logistics_company: A concrete logistics company instance.
        cargo (str): The cargo to be delivered.
        destination (str): The destination address.
        distance_km (float): Distance to destination in kilometers.
    """
    print(f"Client: Planning delivery with {logistics_company.__class__.__name__}")
    print(logistics_company.plan_delivery(cargo, destination, distance_km))
    print()


def demonstrate_logistics_comparison():
    """
    Demonstrate different logistics companies handling the same delivery.
    """
    print("=== Logistics Comparison Demo ===")
    
    # Same delivery requirements
    cargo = "Electronics (500 kg)"
    destination = "New York Port"
    distance_km = 500.0
    
    print(f"Delivery Request:")
    print(f"  Cargo: {cargo}")
    print(f"  Destination: {destination}")
    print(f"  Distance: {distance_km} km")
    print()
    
    # Road Logistics
    road_logistics = RoadLogistics()
    print("🛣️  ROAD LOGISTICS SOLUTION:")
    client_code(road_logistics, cargo, destination, distance_km)
    
    # Sea Logistics
    sea_logistics = SeaLogistics()
    print("🌊 SEA LOGISTICS SOLUTION:")
    client_code(sea_logistics, cargo, destination, distance_km)


def demonstrate_different_scenarios():
    """
    Demonstrate different delivery scenarios with appropriate logistics companies.
    """
    print("=== Different Delivery Scenarios ===")
    
    scenarios = [
        {
            "name": "Domestic Electronics Delivery",
            "cargo": "Laptops (100 kg)",
            "destination": "Local Warehouse, 50 km away",
            "distance": 50.0,
            "logistics": RoadLogistics()
        },
        {
            "name": "International Bulk Cargo",
            "cargo": "Steel Components (10,000 kg)",
            "destination": "Tokyo Port, 8,000 km away",
            "distance": 8000.0,
            "logistics": SeaLogistics()
        },
        {
            "name": "Regional Food Distribution",
            "cargo": "Fresh Produce (2,000 kg)",
            "destination": "Regional Distribution Center, 200 km away",
            "distance": 200.0,
            "logistics": RoadLogistics()
        },
        {
            "name": "Global Oil Transport",
            "cargo": "Crude Oil (50,000,000 kg)",
            "destination": "Rotterdam Port, 12,000 km away",
            "distance": 12000.0,
            "logistics": SeaLogistics()
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"📦 Scenario {i}: {scenario['name']}")
        client_code(
            scenario['logistics'],
            scenario['cargo'],
            scenario['destination'],
            scenario['distance']
        )


def demonstrate_transport_capabilities():
    """
    Demonstrate the capabilities of different transport methods.
    """
    print("=== Transport Capabilities Comparison ===")
    
    road_logistics = RoadLogistics()
    sea_logistics = SeaLogistics()
    
    truck = road_logistics.create_transport()
    ship = sea_logistics.create_transport()
    
    print("🚛 TRUCK CAPABILITIES:")
    print(f"  {truck.get_transport_info()}")
    print(f"  {truck.get_capacity()}")
    print(f"  Cost per km: ${truck.get_cost_per_km()}")
    print()
    
    print("🚢 SHIP CAPABILITIES:")
    print(f"  {ship.get_transport_info()}")
    print(f"  {ship.get_capacity()}")
    print(f"  Cost per km: ${ship.get_cost_per_km()}")
    print()
    
    # Cost comparison for different distances
    distances = [100, 1000, 5000, 10000]
    print("💰 COST COMPARISON:")
    print("Distance (km) | Truck Cost | Ship Cost | Difference")
    print("-" * 50)
    
    for distance in distances:
        truck_cost = distance * truck.get_cost_per_km()
        ship_cost = distance * ship.get_cost_per_km()
        difference = truck_cost - ship_cost
        
        print(f"{distance:>12} | ${truck_cost:>9.2f} | ${ship_cost:>9.2f} | ${difference:>+10.2f}")


def demonstrate_factory_flexibility():
    """
    Demonstrate the flexibility of the Factory Method pattern.
    """
    print("=== Factory Method Flexibility Demo ===")
    
    logistics_companies = [RoadLogistics(), SeaLogistics()]
    
    for logistics in logistics_companies:
        print(f"\n🏢 {logistics.get_company_info()}")
        transport = logistics.create_transport()
        print(f"   Created transport: {transport.__class__.__name__}")
        print(f"   Transport info: {transport.get_transport_info()}")


def main():
    """
    Main function to run all demonstrations.
    """
    print("=== Factory Method Pattern - Logistics Example Demo ===\n")
    
    demonstrate_logistics_comparison()
    demonstrate_different_scenarios()
    demonstrate_transport_capabilities()
    demonstrate_factory_flexibility()
    
    print("\n=== Factory Method Logistics Example Demo Complete ===")


if __name__ == "__main__":
    main()
