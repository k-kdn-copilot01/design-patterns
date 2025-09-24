"""
Flyweight Pattern - Cấu trúc cơ bản

Flyweight Pattern giúp giảm thiểu việc sử dụng bộ nhớ bằng cách chia sẻ
hiệu quả các phần dữ liệu chung giữa nhiều đối tượng.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class Flyweight(ABC):
    """
    Interface Flyweight khai báo phương thức mà concrete flyweight 
    có thể nhận và tác động lên extrinsic state.
    """
    
    @abstractmethod
    def operation(self, extrinsic_state: Dict[str, Any]) -> None:
        """
        Thực hiện operation với extrinsic state được truyền từ bên ngoài.
        
        Args:
            extrinsic_state: Trạng thái ngoại lai được truyền từ context
        """
        pass


class ConcreteFlyweight(Flyweight):
    """
    Concrete Flyweight implement Flyweight interface và lưu trữ intrinsic state.
    Intrinsic state phải độc lập với ngữ cảnh để có thể chia sẻ giữa nhiều contexts.
    """
    
    def __init__(self, intrinsic_state: str):
        """
        Khởi tạo với intrinsic state - dữ liệu được chia sẻ.
        
        Args:
            intrinsic_state: Trạng thái nội tại không thay đổi
        """
        self._intrinsic_state = intrinsic_state
    
    def operation(self, extrinsic_state: Dict[str, Any]) -> None:
        """
        Thực hiện operation kết hợp intrinsic và extrinsic state.
        
        Args:
            extrinsic_state: Trạng thái ngoại lai từ context
        """
        print(f"ConcreteFlyweight: Intrinsic='{self._intrinsic_state}', "
              f"Extrinsic={extrinsic_state}")


class FlyweightFactory:
    """
    Factory quản lý và chia sẻ các flyweight instances.
    Đảm bảo rằng flyweight được chia sẻ đúng cách và không tạo ra duplicate instances.
    """
    
    _flyweights: Dict[str, Flyweight] = {}
    
    def __init__(self, initial_flyweights: list = None):
        """
        Khởi tạo factory với các flyweight ban đầu.
        
        Args:
            initial_flyweights: List các intrinsic state để tạo flyweight
        """
        if initial_flyweights:
            for state in initial_flyweights:
                self._flyweights[state] = ConcreteFlyweight(state)
    
    def get_flyweight(self, shared_state: str) -> Flyweight:
        """
        Trả về existing flyweight với shared state hoặc tạo mới nếu chưa có.
        
        Args:
            shared_state: Trạng thái được chia sẻ (intrinsic state)
            
        Returns:
            Flyweight instance
        """
        if shared_state not in self._flyweights:
            print(f"FlyweightFactory: Tạo mới flyweight cho '{shared_state}'")
            self._flyweights[shared_state] = ConcreteFlyweight(shared_state)
        else:
            print(f"FlyweightFactory: Sử dụng lại flyweight cho '{shared_state}'")
        
        return self._flyweights[shared_state]
    
    def list_flyweights(self) -> None:
        """
        In ra danh sách các flyweight hiện có trong factory.
        """
        count = len(self._flyweights)
        print(f"FlyweightFactory: Có {count} flyweight(s):")
        for key in self._flyweights.keys():
            print(f"  - {key}")


class Context:
    """
    Context chứa extrinsic state và tham chiếu đến flyweight.
    Context truyền extrinsic state cho flyweight methods.
    """
    
    def __init__(self, flyweight: Flyweight, extrinsic_state: Dict[str, Any]):
        """
        Khởi tạo context với flyweight và extrinsic state.
        
        Args:
            flyweight: Flyweight instance được chia sẻ
            extrinsic_state: Trạng thái ngoại lai riêng của context này
        """
        self._flyweight = flyweight
        self._extrinsic_state = extrinsic_state
    
    def operation(self) -> None:
        """
        Thực hiện operation bằng cách delegate cho flyweight với extrinsic state.
        """
        self._flyweight.operation(self._extrinsic_state)
