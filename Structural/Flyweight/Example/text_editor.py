"""
Text Editor - Context class cho Flyweight Pattern

Text Editor quản lý văn bản và formatting, sử dụng Character Flyweights
để tiết kiệm bộ nhớ khi có nhiều ký tự trùng lặp.
"""

from typing import List, Tuple
from character_flyweight import CharacterFactory, CharacterFlyweight


class CharacterContext:
    """
    Context cho mỗi ký tự trong văn bản.
    Chứa extrinsic state: vị trí, font size, màu sắc.
    """
    
    def __init__(self, character: str, position: Tuple[int, int], 
                 font_size: int = 12, color: str = "black"):
        """
        Khởi tạo character context.
        
        Args:
            character: Ký tự (sẽ lấy flyweight từ factory)
            position: Vị trí (x, y) trong văn bản
            font_size: Kích thước font
            color: Màu sắc
        """
        self._flyweight = CharacterFactory.get_character(character)
        self._position = position      # Extrinsic state
        self._font_size = font_size    # Extrinsic state
        self._color = color           # Extrinsic state
    
    def render(self) -> None:
        """
        Render ký tự bằng cách delegate cho flyweight với extrinsic state.
        """
        self._flyweight.render(self._position, self._font_size, self._color)
    
    def get_character(self) -> str:
        """
        Trả về ký tự.
        
        Returns:
            Ký tự string
        """
        return self._flyweight.get_character()
    
    def update_position(self, position: Tuple[int, int]) -> None:
        """
        Cập nhật vị trí của ký tự.
        
        Args:
            position: Vị trí mới (x, y)
        """
        self._position = position
    
    def update_formatting(self, font_size: int = None, color: str = None) -> None:
        """
        Cập nhật formatting của ký tự.
        
        Args:
            font_size: Kích thước font mới (optional)
            color: Màu sắc mới (optional)
        """
        if font_size is not None:
            self._font_size = font_size
        if color is not None:
            self._color = color


class TextEditor:
    """
    Text Editor chính - quản lý toàn bộ văn bản.
    Sử dụng Character Flyweights để optimize memory usage.
    """
    
    def __init__(self):
        """
        Khởi tạo text editor rỗng.
        """
        self._characters: List[CharacterContext] = []
        self._cursor_position = (0, 0)
    
    def type_text(self, text: str, font_size: int = 12, color: str = "black") -> None:
        """
        Nhập văn bản vào editor.
        
        Args:
            text: Văn bản cần nhập
            font_size: Kích thước font
            color: Màu sắc
        """
        x, y = self._cursor_position
        
        for char in text:
            if char == '\n':
                # Newline: di chuyển cursor xuống dòng mới
                x = 0
                y += 20  # Giả sử line height = 20
            else:
                # Tạo character context mới
                position = (x, y)
                char_context = CharacterContext(char, position, font_size, color)
                self._characters.append(char_context)
                
                # Di chuyển cursor
                x += 10  # Giả sử character width = 10
        
        self._cursor_position = (x, y)
    
    def render_document(self) -> None:
        """
        Render toàn bộ văn bản.
        """
        print("📄 Rendering document:")
        print("-" * 50)
        for char_context in self._characters:
            char_context.render()
        print("-" * 50)
    
    def get_text(self) -> str:
        """
        Trả về văn bản hiện tại dưới dạng string.
        
        Returns:
            Văn bản string
        """
        return ''.join(char_context.get_character() for char_context in self._characters)
    
    def format_range(self, start: int, end: int, font_size: int = None, color: str = None) -> None:
        """
        Format một đoạn văn bản.
        
        Args:
            start: Vị trí bắt đầu
            end: Vị trí kết thúc
            font_size: Kích thước font mới
            color: Màu sắc mới
        """
        if start < 0 or end > len(self._characters) or start >= end:
            print("❌ Invalid range!")
            return
        
        print(f"🎨 Formatting characters {start}-{end}...")
        for i in range(start, end):
            self._characters[i].update_formatting(font_size, color)
    
    def get_statistics(self) -> dict:
        """
        Trả về thống kê về văn bản và flyweight usage.
        
        Returns:
            Dictionary chứa thống kê
        """
        total_chars = len(self._characters)
        unique_chars = CharacterFactory.get_created_characters_count()
        
        # Đếm frequency của từng ký tự
        char_frequency = {}
        for char_context in self._characters:
            char = char_context.get_character()
            char_frequency[char] = char_frequency.get(char, 0) + 1
        
        return {
            'total_characters': total_chars,
            'unique_characters': unique_chars,
            'flyweight_objects': unique_chars,
            'context_objects': total_chars,
            'memory_saved_percentage': ((total_chars - unique_chars) / total_chars * 100) if total_chars > 0 else 0,
            'character_frequency': char_frequency
        }
    
    def print_statistics(self) -> None:
        """
        In thống kê về văn bản và hiệu quả của Flyweight Pattern.
        """
        stats = self.get_statistics()
        
        print("\n📊 Text Editor Statistics:")
        print("=" * 40)
        print(f"📝 Total characters: {stats['total_characters']}")
        print(f"🔤 Unique characters: {stats['unique_characters']}")
        print(f"🏭 Flyweight objects: {stats['flyweight_objects']}")
        print(f"📋 Context objects: {stats['context_objects']}")
        print(f"💾 Memory saved: {stats['memory_saved_percentage']:.1f}%")
        print(f"🔍 Memory usage: {CharacterFactory.get_memory_usage()}")
        
        print(f"\n📈 Character frequency:")
        for char, freq in sorted(stats['character_frequency'].items()):
            if char == ' ':
                print(f"   '[space]': {freq}")
            elif char == '\n':
                print(f"   '[newline]': {freq}")
            else:
                print(f"   '{char}': {freq}")
    
    def clear(self) -> None:
        """
        Xóa toàn bộ văn bản.
        """
        self._characters.clear()
        self._cursor_position = (0, 0)
        print("🗑️ Document cleared!")
    
    def __len__(self) -> int:
        """
        Trả về số ký tự trong văn bản.
        
        Returns:
            Số ký tự
        """
        return len(self._characters)
