from typing import List
from FileSystemComponent import FileSystemComponent


class Directory(FileSystemComponent):
    """
    Represents a directory in the file system.
    """
    
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []
    
    def get_size(self) -> int:
        """
        Calculate the total size of the directory and all its contents.
        """
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size
    
    def display(self, indent: int = 0) -> str:
        """
        Display the directory and all its contents with proper indentation.
        """
        result = "  " * indent + f"📁 {self.name}/ ({self.get_size()} bytes)\n"
        for child in self.children:
            result += child.display(indent + 1) + "\n"
        return result.rstrip()
    
    def add(self, component: FileSystemComponent) -> None:
        """
        Add a child component to this directory.
        """
        self.children.append(component)
        component.set_parent(self)
    
    def remove(self, component: FileSystemComponent) -> None:
        """
        Remove a child component from this directory.
        """
        if component in self.children:
            self.children.remove(component)
            component.set_parent(None)
    
    def get_children(self) -> List[FileSystemComponent]:
        """
        Get all child components.
        """
        return self.children.copy()
    
    def is_directory(self) -> bool:
        """
        This is a directory.
        """
        return True
    
    def find_file(self, name: str) -> FileSystemComponent:
        """
        Find a file or directory by name in this directory and its subdirectories.
        """
        for child in self.children:
            if child.name == name:
                return child
            if child.is_directory():
                result = child.find_file(name)
                if result:
                    return result
        return None
