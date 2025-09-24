"""
Demo cơ bản của Flyweight Pattern

Ví dụ này minh họa cách Flyweight Pattern giúp tiết kiệm bộ nhớ
bằng cách chia sẻ các object có intrinsic state giống nhau.
"""

from flyweight import FlyweightFactory, Context


def demo_basic_flyweight():
    """
    Demo cơ bản về Flyweight Pattern.
    Tạo nhiều context với cùng shared state để thể hiện việc chia sẻ flyweight.
    """
    print("=== Demo Flyweight Pattern ===\n")
    
    # Tạo factory với một số flyweight ban đầu
    factory = FlyweightFactory(["Type A", "Type B"])
    factory.list_flyweights()
    print()
    
    # Tạo các context với extrinsic state khác nhau
    contexts = []
    
    # Context 1: Type A với extrinsic state riêng
    flyweight1 = factory.get_flyweight("Type A")
    context1 = Context(flyweight1, {"position": (10, 20), "color": "red"})
    contexts.append(context1)
    
    # Context 2: Type A với extrinsic state khác
    flyweight2 = factory.get_flyweight("Type A")  # Sẽ sử dụng lại flyweight
    context2 = Context(flyweight2, {"position": (30, 40), "color": "blue"})
    contexts.append(context2)
    
    # Context 3: Type B
    flyweight3 = factory.get_flyweight("Type B")
    context3 = Context(flyweight3, {"position": (50, 60), "color": "green"})
    contexts.append(context3)
    
    # Context 4: Type C (mới)
    flyweight4 = factory.get_flyweight("Type C")  # Sẽ tạo mới
    context4 = Context(flyweight4, {"position": (70, 80), "color": "yellow"})
    contexts.append(context4)
    
    print(f"\nSố flyweight objects: {len(factory._flyweights)}")
    print(f"Số context objects: {len(contexts)}")
    print("=> Tiết kiệm bộ nhớ: 4 contexts chỉ sử dụng 3 flyweight objects\n")
    
    # Thực hiện operations
    print("=== Thực hiện operations ===")
    for i, context in enumerate(contexts, 1):
        print(f"Context {i}:")
        context.operation()
        print()
    
    # Hiển thị danh sách flyweight cuối cùng
    print("=== Flyweight objects cuối cùng ===")
    factory.list_flyweights()


def demo_memory_comparison():
    """
    Demo so sánh việc sử dụng bộ nhớ với và không có Flyweight Pattern.
    """
    print("\n" + "="*50)
    print("=== So sánh sử dụng bộ nhớ ===")
    print("="*50)
    
    # Scenario: 1000 objects với 10 shared types
    num_objects = 1000
    shared_types = [f"Type_{i}" for i in range(10)]
    
    print(f"Scenario: {num_objects} objects với {len(shared_types)} shared types")
    print()
    
    # Với Flyweight Pattern
    factory = FlyweightFactory()
    contexts = []
    
    for i in range(num_objects):
        shared_type = shared_types[i % len(shared_types)]
        flyweight = factory.get_flyweight(shared_type)
        extrinsic_state = {"id": i, "position": (i*10, i*20)}
        context = Context(flyweight, extrinsic_state)
        contexts.append(context)
    
    print(f"✅ Với Flyweight Pattern:")
    print(f"   - Số flyweight objects: {len(factory._flyweights)}")
    print(f"   - Số context objects: {len(contexts)}")
    print(f"   - Tổng objects: {len(factory._flyweights) + len(contexts)}")
    
    print(f"\n❌ Không có Flyweight Pattern:")
    print(f"   - Số objects cần tạo: {num_objects}")
    print(f"   - Mỗi object chứa cả intrinsic và extrinsic state")
    
    print(f"\n💡 Tiết kiệm: {num_objects - len(factory._flyweights)} objects!")
    print(f"   Giảm {((num_objects - len(factory._flyweights)) / num_objects * 100):.1f}% số object cần tạo")


if __name__ == "__main__":
    demo_basic_flyweight()
    demo_memory_comparison()
