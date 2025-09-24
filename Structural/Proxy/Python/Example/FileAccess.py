"""
Real-world example: File Access System using Proxy pattern.
Demonstrates access control, logging, and lazy loading for file operations.
"""

import os
import time
from abc import ABC, abstractmethod


class FileAccess(ABC):
    """Abstract interface for file access operations."""
    
    @abstractmethod
    def read_file(self, filename: str) -> str:
        """Read content from a file."""
        pass
    
    @abstractmethod
    def write_file(self, filename: str, content: str) -> bool:
        """Write content to a file."""
        pass


class RealFileAccess(FileAccess):
    """Real file access implementation that performs actual file operations."""
    
    def read_file(self, filename: str) -> str:
        """
        Read content from a file.
        
        Args:
            filename (str): Path to the file to read
            
        Returns:
            str: Content of the file
        """
        print(f"RealFileAccess: Reading file '{filename}'...")
        
        # Simulate file reading delay
        time.sleep(0.1)
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            print(f"RealFileAccess: Successfully read {len(content)} characters from '{filename}'")
            return content
        except FileNotFoundError:
            print(f"RealFileAccess: File '{filename}' not found")
            return f"Error: File '{filename}' not found"
        except Exception as e:
            print(f"RealFileAccess: Error reading file '{filename}': {e}")
            return f"Error: {e}"
    
    def write_file(self, filename: str, content: str) -> bool:
        """
        Write content to a file.
        
        Args:
            filename (str): Path to the file to write
            content (str): Content to write to the file
            
        Returns:
            bool: True if successful, False otherwise
        """
        print(f"RealFileAccess: Writing {len(content)} characters to '{filename}'...")
        
        # Simulate file writing delay
        time.sleep(0.1)
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"RealFileAccess: Successfully wrote to '{filename}'")
            return True
        except Exception as e:
            print(f"RealFileAccess: Error writing to '{filename}': {e}")
            return False


class FileAccessProxy(FileAccess):
    """Proxy for file access with access control, logging, and caching."""
    
    def __init__(self, user_role: str = "guest"):
        """
        Initialize the file access proxy.
        
        Args:
            user_role (str): Role of the user (admin, user, guest)
        """
        self._real_file_access = None
        self._user_role = user_role
        self._access_log = []
        self._cache = {}
        
        # Define access permissions
        self._permissions = {
            "admin": ["read", "write", "delete"],
            "user": ["read", "write"],
            "guest": ["read"]
        }
    
    def _log_access(self, operation: str, filename: str, success: bool):
        """Log file access attempts."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {self._user_role}: {operation} '{filename}' - {'SUCCESS' if success else 'DENIED'}"
        self._access_log.append(log_entry)
        print(f"FileAccessProxy: {log_entry}")
    
    def _check_permission(self, operation: str) -> bool:
        """Check if the user has permission for the operation."""
        return operation in self._permissions.get(self._user_role, [])
    
    def _get_real_file_access(self):
        """Lazy initialization of RealFileAccess."""
        if self._real_file_access is None:
            print("FileAccessProxy: Creating RealFileAccess instance...")
            self._real_file_access = RealFileAccess()
        return self._real_file_access
    
    def read_file(self, filename: str) -> str:
        """
        Read file with access control and caching.
        
        Args:
            filename (str): Path to the file to read
            
        Returns:
            str: Content of the file or error message
        """
        print(f"FileAccessProxy: Intercepting read request for '{filename}'...")
        
        # Check permissions
        if not self._check_permission("read"):
            self._log_access("read", filename, False)
            return f"Access denied: '{self._user_role}' role cannot read files"
        
        # Check cache first
        if filename in self._cache:
            print(f"FileAccessProxy: Returning cached content for '{filename}'")
            self._log_access("read", filename, True)
            return f"[CACHED] {self._cache[filename]}"
        
        # Delegate to real file access
        print(f"FileAccessProxy: Delegating read request to RealFileAccess...")
        real_access = self._get_real_file_access()
        content = real_access.read_file(filename)
        
        # Cache the result if successful
        if not content.startswith("Error:"):
            self._cache[filename] = content
            print(f"FileAccessProxy: Cached content for '{filename}'")
        
        self._log_access("read", filename, not content.startswith("Error:"))
        return content
    
    def write_file(self, filename: str, content: str) -> bool:
        """
        Write file with access control.
        
        Args:
            filename (str): Path to the file to write
            content (str): Content to write to the file
            
        Returns:
            bool: True if successful, False otherwise
        """
        print(f"FileAccessProxy: Intercepting write request for '{filename}'...")
        
        # Check permissions
        if not self._check_permission("write"):
            self._log_access("write", filename, False)
            print(f"FileAccessProxy: Access denied - '{self._user_role}' role cannot write files")
            return False
        
        # Delegate to real file access
        print(f"FileAccessProxy: Delegating write request to RealFileAccess...")
        real_access = self._get_real_file_access()
        success = real_access.write_file(filename, content)
        
        # Clear cache for this file if write was successful
        if success and filename in self._cache:
            del self._cache[filename]
            print(f"FileAccessProxy: Cleared cache for '{filename}'")
        
        self._log_access("write", filename, success)
        return success
    
    def get_access_log(self) -> list:
        """Get the access log."""
        return self._access_log.copy()
    
    def clear_cache(self):
        """Clear the file cache."""
        self._cache.clear()
        print("FileAccessProxy: Cache cleared")
