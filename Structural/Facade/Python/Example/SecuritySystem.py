"""
SecuritySystem - Manages security features in a smart home.
This represents a complex subsystem that handles security operations.
"""

class SecuritySystem:
    """Manages security including locks, cameras, and alarms."""
    
    def __init__(self):
        """Initialize the security system."""
        self.main_door_locked = True
        self.back_door_locked = True
        self.windows_locked = True
        self.cameras_on = True
        self.alarm_armed = True
        self.motion_detection = True
        self.entry_log = []
    
    def lock_main_door(self):
        """Lock the main door."""
        self.main_door_locked = True
        print("🔒 Main door LOCKED")
        self._log_entry("Main door locked")
        return "Main door: LOCKED"
    
    def unlock_main_door(self):
        """Unlock the main door."""
        self.main_door_locked = False
        print("🔓 Main door UNLOCKED")
        self._log_entry("Main door unlocked")
        return "Main door: UNLOCKED"
    
    def lock_back_door(self):
        """Lock the back door."""
        self.back_door_locked = True
        print("🔒 Back door LOCKED")
        self._log_entry("Back door locked")
        return "Back door: LOCKED"
    
    def unlock_back_door(self):
        """Unlock the back door."""
        self.back_door_locked = False
        print("🔓 Back door UNLOCKED")
        self._log_entry("Back door unlocked")
        return "Back door: UNLOCKED"
    
    def lock_all_windows(self):
        """Lock all windows."""
        self.windows_locked = True
        print("🔒 All windows LOCKED")
        self._log_entry("All windows locked")
        return "All windows: LOCKED"
    
    def unlock_all_windows(self):
        """Unlock all windows."""
        self.windows_locked = False
        print("🔓 All windows UNLOCKED")
        self._log_entry("All windows unlocked")
        return "All windows: UNLOCKED"
    
    def turn_on_cameras(self):
        """Turn on security cameras."""
        self.cameras_on = True
        print("📹 Security cameras turned ON")
        return "Cameras: ON"
    
    def turn_off_cameras(self):
        """Turn off security cameras."""
        self.cameras_on = False
        print("📹 Security cameras turned OFF")
        return "Cameras: OFF"
    
    def arm_alarm(self):
        """Arm the security alarm."""
        self.alarm_armed = True
        print("🚨 Security alarm ARMED")
        return "Alarm: ARMED"
    
    def disarm_alarm(self):
        """Disarm the security alarm."""
        self.alarm_armed = False
        print("🚨 Security alarm DISARMED")
        return "Alarm: DISARMED"
    
    def enable_motion_detection(self):
        """Enable motion detection."""
        self.motion_detection = True
        print("👁️  Motion detection ENABLED")
        return "Motion detection: ON"
    
    def disable_motion_detection(self):
        """Disable motion detection."""
        self.motion_detection = False
        print("👁️  Motion detection DISABLED")
        return "Motion detection: OFF"
    
    def secure_house(self):
        """Secure the entire house."""
        print("🏠 Securing entire house...")
        self.lock_main_door()
        self.lock_back_door()
        self.lock_all_windows()
        self.turn_on_cameras()
        self.arm_alarm()
        self.enable_motion_detection()
        print("🏠 House is now SECURE")
        return "House: SECURE"
    
    def unsecure_house(self):
        """Unsecure the entire house."""
        print("🏠 Unsecuring entire house...")
        self.unlock_main_door()
        self.unlock_back_door()
        self.unlock_all_windows()
        self.turn_off_cameras()
        self.disarm_alarm()
        self.disable_motion_detection()
        print("🏠 House is now UNSECURE")
        return "House: UNSECURE"
    
    def _log_entry(self, action):
        """Log security actions."""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.entry_log.append(f"[{timestamp}] {action}")
    
    def get_security_log(self):
        """Get security activity log."""
        return self.entry_log.copy()
    
    def get_status(self):
        """Get current security status."""
        return {
            'main_door': "LOCKED" if self.main_door_locked else "UNLOCKED",
            'back_door': "LOCKED" if self.back_door_locked else "UNLOCKED",
            'windows': "LOCKED" if self.windows_locked else "UNLOCKED",
            'cameras': "ON" if self.cameras_on else "OFF",
            'alarm': "ARMED" if self.alarm_armed else "DISARMED",
            'motion_detection': "ON" if self.motion_detection else "OFF"
        }
