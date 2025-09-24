"""
SmartHomeFacade - Provides a simplified interface to the complex smart home system.
This Facade demonstrates how to simplify complex home automation operations.
"""

from LightingSystem import LightingSystem
from ClimateSystem import ClimateSystem
from SecuritySystem import SecuritySystem
from EntertainmentSystem import EntertainmentSystem


class SmartHomeFacade:
    """
    The SmartHomeFacade provides a simplified interface to the complex smart home system.
    It coordinates multiple subsystems to provide high-level home automation features.
    """
    
    def __init__(self):
        """Initialize the Smart Home Facade with all subsystem instances."""
        self._lighting = LightingSystem()
        self._climate = ClimateSystem()
        self._security = SecuritySystem()
        self._entertainment = EntertainmentSystem()
    
    def arrive_home(self):
        """
        Welcome home scenario - automatically set up the house for arrival.
        This demonstrates how the Facade simplifies complex multi-system operations.
        """
        print("🏠 WELCOME HOME! Setting up your house...")
        print("=" * 50)
        
        # Unlock doors and disarm security
        self._security.unlock_main_door()
        self._security.disarm_alarm()
        self._security.turn_off_cameras()
        
        # Turn on essential lights
        self._lighting.turn_on_living_room()
        self._lighting.turn_on_kitchen()
        self._lighting.set_brightness(70)
        
        # Set comfortable climate
        self._climate.set_comfort_mode()
        
        # Turn on entertainment
        self._entertainment.turn_on_tv()
        self._entertainment.change_channel(1)
        self._entertainment.set_tv_volume(40)
        
        print("=" * 50)
        print("🏠 Welcome home setup completed!")
        return "Welcome home: Setup completed"
    
    def leave_home(self):
        """
        Leave home scenario - automatically secure the house when leaving.
        This demonstrates how the Facade coordinates security and energy saving.
        """
        print("🏠 LEAVING HOME! Securing your house...")
        print("=" * 50)
        
        # Secure the house
        self._security.secure_house()
        
        # Turn off all lights to save energy
        self._lighting.turn_off_all_lights()
        
        # Set energy saving mode
        self._climate.set_energy_save_mode()
        
        # Turn off all entertainment
        self._entertainment.turn_off_all_entertainment()
        
        print("=" * 50)
        print("🏠 House secured! Have a great day!")
        return "Leave home: House secured"
    
    def movie_night(self):
        """
        Movie night scenario - set up the perfect environment for watching movies.
        This demonstrates how the Facade creates themed experiences.
        """
        print("🎬 MOVIE NIGHT! Setting up the perfect environment...")
        print("=" * 50)
        
        # Dim the lights for movie atmosphere
        self._lighting.turn_off_all_lights()
        self._lighting.turn_on_living_room()
        self._lighting.set_brightness(20)
        
        # Set comfortable temperature
        self._climate.set_temperature(21)
        self._climate.start_ventilation()
        
        # Set up entertainment for movies
        self._entertainment.set_movie_mode()
        
        print("=" * 50)
        print("🎬 Movie night setup completed! Enjoy your movie!")
        return "Movie night: Setup completed"
    
    def party_mode(self):
        """
        Party mode scenario - create a festive atmosphere for parties.
        This demonstrates how the Facade coordinates multiple systems for events.
        """
        print("🎉 PARTY MODE! Creating a festive atmosphere...")
        print("=" * 50)
        
        # Bright lighting for party atmosphere
        self._lighting.turn_on_all_lights()
        self._lighting.set_brightness(90)
        
        # Comfortable climate with ventilation
        self._climate.set_comfort_mode()
        
        # Party entertainment setup
        self._entertainment.set_party_mode()
        
        # Unlock doors for guests (but keep security cameras on)
        self._security.unlock_main_door()
        self._security.unlock_back_door()
        self._security.turn_on_cameras()
        self._security.disable_motion_detection()  # Avoid false alarms during party
        
        print("=" * 50)
        print("🎉 Party mode activated! Let's celebrate!")
        return "Party mode: Activated"
    
    def sleep_mode(self):
        """
        Sleep mode scenario - prepare the house for a good night's sleep.
        This demonstrates how the Facade creates a peaceful environment.
        """
        print("😴 SLEEP MODE! Preparing for a good night's sleep...")
        print("=" * 50)
        
        # Turn off most lights, keep bedroom light dim
        self._lighting.turn_off_all_lights()
        self._lighting.turn_on_bedroom()
        self._lighting.set_brightness(10)
        
        # Set comfortable sleeping temperature
        self._climate.set_temperature(19)
        self._climate.set_humidity(50)
        self._climate.stop_ventilation()
        
        # Turn off all entertainment
        self._entertainment.turn_off_all_entertainment()
        
        # Secure the house for the night
        self._security.secure_house()
        
        print("=" * 50)
        print("😴 Sleep mode activated! Sweet dreams!")
        return "Sleep mode: Activated"
    
    def emergency_mode(self):
        """
        Emergency mode scenario - secure the house and alert systems.
        This demonstrates how the Facade handles emergency situations.
        """
        print("🚨 EMERGENCY MODE! Activating security protocols...")
        print("=" * 50)
        
        # Full security activation
        self._security.secure_house()
        self._security.arm_alarm()
        self._security.turn_on_cameras()
        self._security.enable_motion_detection()
        
        # Turn on all lights for visibility
        self._lighting.turn_on_all_lights()
        self._lighting.set_brightness(100)
        
        # Turn off entertainment to focus on emergency
        self._entertainment.turn_off_all_entertainment()
        
        print("=" * 50)
        print("🚨 Emergency mode activated! All systems secured!")
        return "Emergency mode: Activated"
    
    def get_home_status(self):
        """
        Get comprehensive status of all home systems.
        This demonstrates how the Facade provides unified status information.
        """
        print("📊 HOME STATUS REPORT")
        print("=" * 50)
        
        lighting_status = self._lighting.get_status()
        climate_status = self._climate.get_status()
        security_status = self._security.get_status()
        entertainment_status = self._entertainment.get_status()
        
        print("💡 LIGHTING:")
        for status in lighting_status:
            print(f"   {status}")
        
        print("\n🌡️  CLIMATE:")
        for key, value in climate_status.items():
            print(f"   {key.replace('_', ' ').title()}: {value}")
        
        print("\n🔒 SECURITY:")
        for key, value in security_status.items():
            print(f"   {key.replace('_', ' ').title()}: {value}")
        
        print("\n🎵 ENTERTAINMENT:")
        for key, value in entertainment_status.items():
            if value is not None:
                print(f"   {key.replace('_', ' ').title()}: {value}")
        
        print("=" * 50)
        return "Home status report completed"
    
    # Individual system access methods
    def get_lighting_system(self):
        """Get access to the lighting system."""
        return self._lighting
    
    def get_climate_system(self):
        """Get access to the climate system."""
        return self._climate
    
    def get_security_system(self):
        """Get access to the security system."""
        return self._security
    
    def get_entertainment_system(self):
        """Get access to the entertainment system."""
        return self._entertainment
