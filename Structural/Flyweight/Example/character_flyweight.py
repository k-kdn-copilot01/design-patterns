"""
Character Flyweight - Ví dụ thực tế về Text Editor

Flyweight Pattern được áp dụng cho các ký tự trong text editor.
Mỗi ký tự có thể xuất hiện nhiều lần trong văn bản, nhưng chúng ta
chỉ cần lưu trữ một instance cho mỗi ký tự duy nhất.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any
import sys


class CharacterFlyweight(ABC):
    """
    Abstract Flyweight interface cho characters.
    """
    
    @abstractmethod
    def render(self, position: tuple, font_size: int, color: str) -> None:
        """
        Render character tại vị trí cụ thể với formatting.
        
        Args:
            position: Vị trí (x, y) của character
            font_size: Kích thước font
            color: Màu sắc
        """
        pass
    
    @abstractmethod
    def get_character(self) -> str:
        """
        Trả về ký tự mà flyweight này đại diện.
        
        Returns:
            Ký tự string
        """
        pass


class ConcreteCharacter(CharacterFlyweight):
    """
    Concrete Character Flyweight.
    Lưu trữ intrinsic state (ký tự) và implement render method.
    """
    
    def __init__(self, character: str):
        """
        Khởi tạo với ký tự cụ thể (intrinsic state).
        
        Args:
            character: Ký tự được đại diện bởi flyweight này
        """
        self._character = character  # Intrinsic state
    
    def render(self, position: tuple, font_size: int, color: str) -> None:
        """
        Render character với extrinsic state.
        
        Args:
            position: Vị trí (x, y) - extrinsic state
            font_size: Kích thước font - extrinsic state  
            color: Màu sắc - extrinsic state
        """
        x, y = position
        print(f"Rendering '{self._character}' at ({x:3d},{y:3d}) "
              f"size={font_size:2d} color={color}")
    
    def get_character(self) -> str:
        """
        Trả về ký tự.
        
        Returns:
            Ký tự string
        """
        return self._character
    
    def __repr__(self) -> str:
        return f"ConcreteCharacter('{self._character}')"


class CharacterFactory:
    """
    Factory quản lý Character Flyweights.
    Đảm bảo rằng mỗi ký tự chỉ có một flyweight instance.
    """
    
    _characters: Dict[str, CharacterFlyweight] = {}
    
    @classmethod
    def get_character(cls, character: str) -> CharacterFlyweight:
        """
        Trả về flyweight cho ký tự, tạo mới nếu chưa tồn tại.
        
        Args:
            character: Ký tự cần flyweight
            
        Returns:
            CharacterFlyweight instance
        """
        if character not in cls._characters:
            print(f"📝 Tạo flyweight mới cho ký tự: '{character}'")
            cls._characters[character] = ConcreteCharacter(character)
        
        return cls._characters[character]
    
    @classmethod
    def get_created_characters_count(cls) -> int:
        """
        Trả về số lượng character flyweight đã tạo.
        
        Returns:
            Số lượng flyweight
        """
        return len(cls._characters)
    
    @classmethod
    def list_created_characters(cls) -> None:
        """
        In danh sách các character flyweight đã tạo.
        """
        print(f"🔍 Character Flyweights đã tạo ({len(cls._characters)}):")
        for char in sorted(cls._characters.keys()):
            print(f"   '{char}' -> {cls._characters[char]}")
    
    @classmethod
    def get_memory_usage(cls) -> str:
        """
        Ước tính memory usage của flyweight objects.
        
        Returns:
            String mô tả memory usage
        """
        # Ước tính size của mỗi flyweight object
        flyweight_size = sys.getsizeof(ConcreteCharacter('a'))
        total_size = len(cls._characters) * flyweight_size
        return f"{total_size} bytes ({len(cls._characters)} objects × {flyweight_size} bytes)"
    
    @classmethod
    def reset(cls) -> None:
        """
        Reset factory - xóa tất cả flyweight đã tạo.
        Chỉ dùng cho testing/demo.
        """
        cls._characters.clear()
        print("🔄 Factory đã được reset")
