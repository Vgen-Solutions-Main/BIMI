"""
Core IBIM implementation module
"""

from typing import Dict, List, Any, Optional


class Component:
    """
    Represents a component in the IBIM system.
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        """
        Initialize a component.
        
        Args:
            name: The component name
            config: Optional configuration dictionary
        """
        self.name = name
        self.config = config or {}
        self.status = "initialized"
    
    def process(self) -> Dict[str, Any]:
        """
        Process the component.
        
        Returns:
            Dictionary with processing results
        """
        self.status = "processed"
        return {
            "name": self.name,
            "status": self.status,
            "config": self.config
        }
    
    def __repr__(self) -> str:
        return f"Component(name='{self.name}', status='{self.status}')"


class IBIM:
    """
    Main IBIM class for managing components and processing.
    """
    
    def __init__(self, name: str = "IBIM"):
        """
        Initialize the IBIM instance.
        
        Args:
            name: The IBIM instance name
        """
        self.name = name
        self.components: Dict[str, Component] = {}
        self.results: List[Dict[str, Any]] = []
    
    def add_component(self, name: str, config: Optional[Dict[str, Any]] = None) -> Component:
        """
        Add a new component to the IBIM instance.
        
        Args:
            name: The component name
            config: Optional configuration dictionary
            
        Returns:
            The created Component instance
        """
        component = Component(name, config)
        self.components[name] = component
        return component
    
    def remove_component(self, name: str) -> bool:
        """
        Remove a component from the IBIM instance.
        
        Args:
            name: The component name to remove
            
        Returns:
            True if removed, False if not found
        """
        if name in self.components:
            del self.components[name]
            return True
        return False
    
    def get_component(self, name: str) -> Optional[Component]:
        """
        Get a component by name.
        
        Args:
            name: The component name
            
        Returns:
            The Component instance or None if not found
        """
        return self.components.get(name)
    
    def process(self) -> List[Dict[str, Any]]:
        """
        Process all components in the IBIM instance.
        
        Returns:
            List of processing results from all components
        """
        self.results = []
        for component in self.components.values():
            result = component.process()
            self.results.append(result)
        return self.results
    
    def get_results(self) -> List[Dict[str, Any]]:
        """
        Get the processing results.
        
        Returns:
            List of processing results
        """
        return self.results
    
    def __repr__(self) -> str:
        return f"IBIM(name='{self.name}', components={len(self.components)})"
