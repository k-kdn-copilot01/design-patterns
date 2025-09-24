"""
LightingSystem - Manages all lighting operations in a smart home.
This represents a complex subsystem that handles various lighting scenarios.
"""

class LightingSystem:
    """Manages lighting operations including different rooms and lighting modes."""
    
    def __init__(self):
        """Initialize the lighting system."""
        self.lights = {
            'living_room': False,
            'kitchen': False,
            'bedroom': False,
            'bathroom': False,
            'outdoor': False
        }
        self.brightness = 50  # Default brightness percentage
    
    def turn_on_living_room(self):
        """Turn on living room lights."""
        self.lights['living_room'] = True
        print("💡 Living room lights turned ON")
        return "Living room lights: ON"
    
    def turn_off_living_room(self):
        """Turn off living room lights."""
        self.lights['living_room'] = False
        print("💡 Living room lights turned OFF")
        return "Living room lights: OFF"
    
    def turn_on_kitchen(self):
        """Turn on kitchen lights."""
        self.lights['kitchen'] = True
        print("💡 Kitchen lights turned ON")
        return "Kitchen lights: ON"
    
    def turn_off_kitchen(self):
        """Turn off kitchen lights."""
        self.lights['kitchen'] = False
        print("💡 Kitchen lights turned OFF")
        return "Kitchen lights: OFF"
    
    def turn_on_bedroom(self):
        """Turn on bedroom lights."""
        self.lights['bedroom'] = True
        print("💡 Bedroom lights turned ON")
        return "Bedroom lights: ON"
    
    def turn_off_bedroom(self):
        """Turn off bedroom lights."""
        self.lights['bedroom'] = False
        print("💡 Bedroom lights turned OFF")
        return "Bedroom lights: OFF"
    
    def turn_on_outdoor(self):
        """Turn on outdoor lights."""
        self.lights['outdoor'] = True
        print("💡 Outdoor lights turned ON")
        return "Outdoor lights: ON"
    
    def turn_off_outdoor(self):
        """Turn off outdoor lights."""
        self.lights['outdoor'] = False
        print("💡 Outdoor lights turned OFF")
        return "Outdoor lights: OFF"
    
    def set_brightness(self, level):
        """Set brightness level for all lights."""
        self.brightness = max(0, min(100, level))
        print(f"💡 Brightness set to {self.brightness}%")
        return f"Brightness: {self.brightness}%"
    
    def turn_on_all_lights(self):
        """Turn on all lights in the house."""
        print("💡 Turning on ALL lights...")
        for room in self.lights:
            self.lights[room] = True
        print("💡 All lights are now ON")
        return "All lights: ON"
    
    def turn_off_all_lights(self):
        """Turn off all lights in the house."""
        print("💡 Turning off ALL lights...")
        for room in self.lights:
            self.lights[room] = False
        print("💡 All lights are now OFF")
        return "All lights: OFF"
    
    def get_status(self):
        """Get current status of all lights."""
        status = []
        for room, is_on in self.lights.items():
            status.append(f"{room.replace('_', ' ').title()}: {'ON' if is_on else 'OFF'}")
        return status
