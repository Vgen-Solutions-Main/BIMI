"""
Basic usage example for IBIMjr
"""

import sys
import os

# Add src to path for local imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ibim import IBIM


def main():
    """Demonstrate basic IBIM usage"""
    
    # Create an IBIM instance
    print("Creating IBIM instance...")
    ibim = IBIM(name="ExampleProject")
    print(f"Created: {ibim}\n")
    
    # Add some components
    print("Adding components...")
    component1 = ibim.add_component("DataLoader", {
        "type": "data",
        "source": "example.csv"
    })
    print(f"Added: {component1}")
    
    component2 = ibim.add_component("Processor", {
        "type": "processing",
        "algorithm": "simple"
    })
    print(f"Added: {component2}")
    
    component3 = ibim.add_component("OutputWriter", {
        "type": "output",
        "destination": "results.json"
    })
    print(f"Added: {component3}\n")
    
    # Process all components
    print("Processing components...")
    results = ibim.process()
    
    # Display results
    print("\nProcessing Results:")
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['name']}")
        print(f"   Status: {result['status']}")
        print(f"   Config: {result['config']}")
    
    # Get a specific component
    print("\n\nRetrieving specific component...")
    data_loader = ibim.get_component("DataLoader")
    print(f"Retrieved: {data_loader}")
    
    # Remove a component
    print("\nRemoving component...")
    removed = ibim.remove_component("Processor")
    print(f"Removed 'Processor': {removed}")
    print(f"Updated IBIM: {ibim}")


if __name__ == "__main__":
    main()
