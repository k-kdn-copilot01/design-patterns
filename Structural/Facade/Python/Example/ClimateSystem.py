"""
ClimateSystem - Manages heating, cooling, and ventilation in a smart home.
This represents a complex subsystem that handles climate control operations.
"""

class ClimateSystem:
    """Manages climate control including temperature, humidity, and air quality."""
    
    def __init__(self):
        """Initialize the climate system."""
        self.current_temp = 22  # Celsius
        self.target_temp = 22
        self.humidity = 45  # Percentage
        self.air_quality = "Good"
        self.heating_on = False
        self.cooling_on = False
        self.ventilation_on = False
    
    def set_temperature(self, temp):
        """Set target temperature."""
        self.target_temp = temp
        print(f"🌡️  Target temperature set to {temp}°C")
        
        if temp > self.current_temp:
            self.start_heating()
        elif temp < self.current_temp:
            self.start_cooling()
        else:
            self.stop_heating()
            self.stop_cooling()
        
        return f"Target temperature: {temp}°C"
    
    def start_heating(self):
        """Start heating system."""
        self.heating_on = True
        self.cooling_on = False
        print("🔥 Heating system started")
        return "Heating: ON"
    
    def stop_heating(self):
        """Stop heating system."""
        self.heating_on = False
        print("🔥 Heating system stopped")
        return "Heating: OFF"
    
    def start_cooling(self):
        """Start cooling system."""
        self.cooling_on = True
        self.heating_on = False
        print("❄️  Cooling system started")
        return "Cooling: ON"
    
    def stop_cooling(self):
        """Stop cooling system."""
        self.cooling_on = False
        print("❄️  Cooling system stopped")
        return "Cooling: OFF"
    
    def set_humidity(self, level):
        """Set humidity level."""
        self.humidity = max(0, min(100, level))
        print(f"💧 Humidity set to {self.humidity}%")
        return f"Humidity: {self.humidity}%"
    
    def start_ventilation(self):
        """Start ventilation system."""
        self.ventilation_on = True
        print("💨 Ventilation system started")
        return "Ventilation: ON"
    
    def stop_ventilation(self):
        """Stop ventilation system."""
        self.ventilation_on = False
        print("💨 Ventilation system stopped")
        return "Ventilation: OFF"
    
    def set_comfort_mode(self):
        """Set comfort mode (optimal temperature and humidity)."""
        print("🏠 Setting comfort mode...")
        self.set_temperature(22)
        self.set_humidity(45)
        self.start_ventilation()
        print("🏠 Comfort mode activated")
        return "Comfort mode: ON"
    
    def set_energy_save_mode(self):
        """Set energy saving mode."""
        print("🔋 Setting energy save mode...")
        self.set_temperature(20)
        self.set_humidity(40)
        self.stop_ventilation()
        print("🔋 Energy save mode activated")
        return "Energy save mode: ON"
    
    def get_status(self):
        """Get current climate status."""
        return {
            'temperature': f"{self.current_temp}°C",
            'target_temp': f"{self.target_temp}°C",
            'humidity': f"{self.humidity}%",
            'air_quality': self.air_quality,
            'heating': "ON" if self.heating_on else "OFF",
            'cooling': "ON" if self.cooling_on else "OFF",
            'ventilation': "ON" if self.ventilation_on else "OFF"
        }
