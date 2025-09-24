"""
Demo Text Editor với Flyweight Pattern

Ví dụ thực tế về cách Flyweight Pattern được sử dụng trong một text editor
để tiết kiệm bộ nhớ khi xử lý văn bản có nhiều ký tự trùng lặp.
"""

from text_editor import TextEditor
from character_flyweight import CharacterFactory


def demo_basic_text_editing():
    """
    Demo cơ bản về text editing với flyweight pattern.
    """
    print("=== Demo Text Editor với Flyweight Pattern ===\n")
    
    # Tạo text editor
    editor = TextEditor()
    
    # Nhập một số văn bản
    print("📝 Nhập văn bản...")
    editor.type_text("Hello World!", font_size=12, color="black")
    editor.type_text("\n", font_size=12, color="black")
    editor.type_text("Flyweight Pattern Demo", font_size=14, color="blue")
    
    # Hiển thị văn bản
    print(f"\n📄 Văn bản hiện tại: '{editor.get_text()}'")
    
    # Hiển thị thống kê
    editor.print_statistics()
    
    # Hiển thị các flyweight đã tạo
    print()
    CharacterFactory.list_created_characters()
    
    return editor


def demo_memory_efficiency():
    """
    Demo hiệu quả về memory khi có nhiều ký tự trùng lặp.
    """
    print("\n" + "="*60)
    print("=== Demo hiệu quả Memory với văn bản lớn ===")
    print("="*60)
    
    # Reset factory để demo rõ ràng hơn
    CharacterFactory.reset()
    
    # Tạo editor mới
    editor = TextEditor()
    
    # Nhập văn bản có nhiều ký tự trùng lặp
    repeated_text = "abcdefg" * 20  # 140 ký tự với chỉ 7 ký tự unique
    editor.type_text(repeated_text, font_size=12, color="black")
    
    print(f"📝 Đã nhập {len(repeated_text)} ký tự")
    print(f"🔤 Chỉ có 7 ký tự unique: a, b, c, d, e, f, g")
    
    # Hiển thị thống kê
    editor.print_statistics()
    
    # So sánh với approach không dùng flyweight
    print(f"\n💡 So sánh với approach không dùng Flyweight:")
    print(f"   ❌ Không dùng: {len(repeated_text)} objects")
    print(f"   ✅ Dùng Flyweight: {CharacterFactory.get_created_characters_count()} flyweight + {len(repeated_text)} context")
    print(f"   🎯 Tiết kiệm: {len(repeated_text) - CharacterFactory.get_created_characters_count()} objects!")
    
    return editor


def demo_text_formatting():
    """
    Demo formatting văn bản với flyweight pattern.
    """
    print("\n" + "="*60)
    print("=== Demo Text Formatting ===")
    print("="*60)
    
    # Tạo editor mới
    editor = TextEditor()
    
    # Nhập văn bản với format khác nhau
    print("📝 Tạo văn bản với nhiều format...")
    editor.type_text("Normal text. ", font_size=12, color="black")
    editor.type_text("Bold text. ", font_size=14, color="red")
    editor.type_text("Small text.", font_size=10, color="blue")
    
    print(f"\n📄 Văn bản: '{editor.get_text()}'")
    
    # Render văn bản để thấy format
    editor.render_document()
    
    # Format lại một phần văn bản
    print("\n🎨 Format lại ký tự 0-6 thành màu green, size 16...")
    editor.format_range(0, 6, font_size=16, color="green")
    
    # Render lại
    print("\n📄 Sau khi format:")
    editor.render_document()
    
    # Thống kê
    editor.print_statistics()
    
    return editor


def demo_large_document():
    """
    Demo với văn bản lớn để thể hiện rõ hiệu quả của flyweight.
    """
    print("\n" + "="*60)
    print("=== Demo văn bản lớn (Lorem Ipsum) ===")
    print("="*60)
    
    # Reset factory
    CharacterFactory.reset()
    
    # Tạo editor
    editor = TextEditor()
    
    # Lorem ipsum text với nhiều ký tự trùng lặp
    lorem_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco.
Laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse.
Cillum dolore eu fugiat nulla pariatur excepteur sint occaecat.
Lorem ipsum dolor sit amet, consectetur adipiscing elit."""
    
    print(f"📝 Nhập Lorem Ipsum text ({len(lorem_text)} ký tự)...")
    editor.type_text(lorem_text, font_size=12, color="black")
    
    # Thống kê chi tiết
    editor.print_statistics()
    
    # Hiển thị top 10 ký tự xuất hiện nhiều nhất
    stats = editor.get_statistics()
    sorted_chars = sorted(stats['character_frequency'].items(), 
                         key=lambda x: x[1], reverse=True)
    
    print(f"\n🏆 Top 10 ký tự xuất hiện nhiều nhất:")
    for i, (char, freq) in enumerate(sorted_chars[:10], 1):
        char_display = char if char not in [' ', '\n'] else f"[{char.strip() or 'space'}]"
        print(f"   {i:2d}. '{char_display}': {freq} lần")
    
    # Tính toán memory efficiency
    total_chars = stats['total_characters']
    unique_chars = stats['unique_characters']
    memory_saved = total_chars - unique_chars
    
    print(f"\n💾 Memory Efficiency Analysis:")
    print(f"   📊 Tổng ký tự: {total_chars}")
    print(f"   🔤 Ký tự unique: {unique_chars}")
    print(f"   💰 Objects tiết kiệm: {memory_saved}")
    print(f"   📈 Hiệu quả: {(memory_saved/total_chars)*100:.1f}% reduction")
    
    return editor


def interactive_demo():
    """
    Demo tương tác cho phép user nhập văn bản.
    """
    print("\n" + "="*60)
    print("=== Demo Tương Tác ===")
    print("="*60)
    
    editor = TextEditor()
    
    print("💬 Nhập văn bản (Enter để kết thúc, 'quit' để thoát):")
    
    while True:
        try:
            text = input(">> ")
            if text.lower() == 'quit':
                break
            elif text == '':
                break
            else:
                editor.type_text(text + " ", font_size=12, color="black")
                print(f"📝 Đã thêm: '{text}'")
        except KeyboardInterrupt:
            print("\n👋 Thoát demo...")
            break
    
    if len(editor) > 0:
        print(f"\n📄 Văn bản cuối cùng: '{editor.get_text().strip()}'")
        editor.print_statistics()
        CharacterFactory.list_created_characters()
    else:
        print("📭 Không có văn bản nào được nhập.")


if __name__ == "__main__":
    # Chạy tất cả demo
    try:
        demo_basic_text_editing()
        demo_memory_efficiency()
        demo_text_formatting()
        demo_large_document()
        
        # Uncomment dòng dưới để chạy interactive demo
        # interactive_demo()
        
    except KeyboardInterrupt:
        print("\n\n👋 Demo đã được dừng bởi user.")
    except Exception as e:
        print(f"\n❌ Lỗi trong demo: {e}")
    
    print("\n✅ Demo hoàn thành!")
