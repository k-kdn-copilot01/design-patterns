"""
Real-world example: Configuration Management System

This example demonstrates the Prototype pattern in a practical scenario
where we need to create multiple configuration objects with slight variations
from a base template.
"""

import copy
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class ConfigPrototype(ABC):
    """Abstract base class for configuration prototypes."""
    
    @abstractmethod
    def clone(self) -> 'ConfigPrototype':
        """Create a copy of this configuration."""
        pass
    
    @abstractmethod
    def get_config(self) -> Dict[str, Any]:
        """Get the configuration dictionary."""
        pass
    
    @abstractmethod
    def update_config(self, updates: Dict[str, Any]) -> None:
        """Update configuration with new values."""
        pass


class DatabaseConfig(ConfigPrototype):
    """Database configuration prototype."""
    
    def __init__(self, host: str = "localhost", port: int = 5432, 
                 database: str = "default_db", username: str = "user", 
                 password: str = "password"):
        self.config = {
            "host": host,
            "port": port,
            "database": database,
            "username": username,
            "password": password,
            "connection_pool": {
                "min_connections": 5,
                "max_connections": 20,
                "timeout": 30
            },
            "ssl": {
                "enabled": False,
                "cert_path": None
            }
        }
        print(f"DatabaseConfig created: {database}@{host}:{port}")
    
    def clone(self) -> 'DatabaseConfig':
        """Create a deep copy of this database configuration."""
        cloned = copy.deepcopy(self)
        print(f"DatabaseConfig cloned: {cloned.config['database']}@{cloned.config['host']}:{cloned.config['port']}")
        return cloned
    
    def get_config(self) -> Dict[str, Any]:
        """Get the configuration dictionary."""
        return self.config.copy()
    
    def update_config(self, updates: Dict[str, Any]) -> None:
        """Update configuration with new values."""
        for key, value in updates.items():
            if key in self.config:
                self.config[key] = value
            else:
                print(f"Warning: Unknown config key '{key}' ignored")
    
    def __str__(self) -> str:
        return f"DatabaseConfig({self.config['database']}@{self.config['host']}:{self.config['port']})"


class APIConfig(ConfigPrototype):
    """API configuration prototype."""
    
    def __init__(self, base_url: str = "https://api.example.com", 
                 api_key: str = "default_key", version: str = "v1"):
        self.config = {
            "base_url": base_url,
            "api_key": api_key,
            "version": version,
            "timeout": 30,
            "retry_attempts": 3,
            "rate_limit": {
                "requests_per_minute": 100,
                "burst_limit": 10
            },
            "headers": {
                "User-Agent": "MyApp/1.0",
                "Accept": "application/json"
            }
        }
        print(f"APIConfig created: {base_url}/{version}")
    
    def clone(self) -> 'APIConfig':
        """Create a deep copy of this API configuration."""
        cloned = copy.deepcopy(self)
        print(f"APIConfig cloned: {cloned.config['base_url']}/{cloned.config['version']}")
        return cloned
    
    def get_config(self) -> Dict[str, Any]:
        """Get the configuration dictionary."""
        return self.config.copy()
    
    def update_config(self, updates: Dict[str, Any]) -> None:
        """Update configuration with new values."""
        for key, value in updates.items():
            if key in self.config:
                self.config[key] = value
            else:
                print(f"Warning: Unknown config key '{key}' ignored")
    
    def __str__(self) -> str:
        return f"APIConfig({self.config['base_url']}/{self.config['version']})"


class DocumentTemplate(ConfigPrototype):
    """Document template prototype."""
    
    def __init__(self, title: str = "Untitled Document", 
                 author: str = "System", template_type: str = "default"):
        self.config = {
            "title": title,
            "author": author,
            "template_type": template_type,
            "created_at": None,
            "modified_at": None,
            "metadata": {
                "version": "1.0",
                "language": "en",
                "category": "general"
            },
            "formatting": {
                "font_family": "Arial",
                "font_size": 12,
                "line_spacing": 1.5,
                "margins": {"top": 1, "bottom": 1, "left": 1, "right": 1}
            },
            "content": {
                "sections": [],
                "tables": [],
                "images": []
            }
        }
        print(f"DocumentTemplate created: '{title}' by {author}")
    
    def clone(self) -> 'DocumentTemplate':
        """Create a deep copy of this document template."""
        cloned = copy.deepcopy(self)
        print(f"DocumentTemplate cloned: '{cloned.config['title']}' by {cloned.config['author']}")
        return cloned
    
    def get_config(self) -> Dict[str, Any]:
        """Get the configuration dictionary."""
        return self.config.copy()
    
    def update_config(self, updates: Dict[str, Any]) -> None:
        """Update configuration with new values."""
        for key, value in updates.items():
            if key in self.config:
                self.config[key] = value
            else:
                print(f"Warning: Unknown config key '{key}' ignored")
    
    def add_section(self, title: str, content: str) -> None:
        """Add a section to the document."""
        self.config["content"]["sections"].append({
            "title": title,
            "content": content,
            "order": len(self.config["content"]["sections"]) + 1
        })
    
    def __str__(self) -> str:
        return f"DocumentTemplate('{self.config['title']}' by {self.config['author']})"


class ConfigManager:
    """Manager class for handling configuration prototypes."""
    
    def __init__(self):
        self.prototypes: Dict[str, ConfigPrototype] = {}
        print("ConfigManager initialized")
    
    def register_prototype(self, name: str, prototype: ConfigPrototype) -> None:
        """Register a configuration prototype."""
        self.prototypes[name] = prototype
        print(f"Registered prototype: {name}")
    
    def create_config(self, prototype_name: str, customizations: Optional[Dict[str, Any]] = None) -> ConfigPrototype:
        """Create a new configuration from a prototype with optional customizations."""
        if prototype_name not in self.prototypes:
            raise ValueError(f"No prototype registered with name: {prototype_name}")
        
        # Clone the prototype
        new_config = self.prototypes[prototype_name].clone()
        
        # Apply customizations if provided
        if customizations:
            new_config.update_config(customizations)
            print(f"Applied customizations to {prototype_name}")
        
        return new_config
    
    def list_prototypes(self) -> None:
        """List all registered prototypes."""
        print("\\nRegistered prototypes:")
        for name, prototype in self.prototypes.items():
            print(f"  - {name}: {prototype}")
    
    def get_prototype(self, name: str) -> ConfigPrototype:
        """Get a registered prototype by name."""
        if name not in self.prototypes:
            raise ValueError(f"No prototype registered with name: {name}")
        return self.prototypes[name]
