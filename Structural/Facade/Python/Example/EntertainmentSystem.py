"""
EntertainmentSystem - Manages entertainment devices in a smart home.
This represents a complex subsystem that handles entertainment operations.
"""

class EntertainmentSystem:
    """Manages entertainment including TV, music, and gaming systems."""
    
    def __init__(self):
        """Initialize the entertainment system."""
        self.tv_on = False
        self.tv_channel = 1
        self.tv_volume = 50
        self.music_system_on = False
        self.music_volume = 30
        self.current_song = None
        self.gaming_system_on = False
        self.current_game = None
    
    def turn_on_tv(self):
        """Turn on the TV."""
        self.tv_on = True
        print("📺 TV turned ON")
        return "TV: ON"
    
    def turn_off_tv(self):
        """Turn off the TV."""
        self.tv_on = False
        print("📺 TV turned OFF")
        return "TV: OFF"
    
    def change_channel(self, channel):
        """Change TV channel."""
        self.tv_channel = channel
        print(f"📺 Channel changed to {channel}")
        return f"TV Channel: {channel}"
    
    def set_tv_volume(self, volume):
        """Set TV volume."""
        self.tv_volume = max(0, min(100, volume))
        print(f"📺 TV volume set to {self.tv_volume}")
        return f"TV Volume: {self.tv_volume}"
    
    def turn_on_music_system(self):
        """Turn on music system."""
        self.music_system_on = True
        print("🎵 Music system turned ON")
        return "Music system: ON"
    
    def turn_off_music_system(self):
        """Turn off music system."""
        self.music_system_on = False
        print("🎵 Music system turned OFF")
        return "Music system: OFF"
    
    def play_music(self, song):
        """Play a specific song."""
        self.current_song = song
        print(f"🎵 Now playing: {song}")
        return f"Playing: {song}"
    
    def set_music_volume(self, volume):
        """Set music volume."""
        self.music_volume = max(0, min(100, volume))
        print(f"🎵 Music volume set to {self.music_volume}")
        return f"Music Volume: {self.music_volume}"
    
    def turn_on_gaming_system(self):
        """Turn on gaming system."""
        self.gaming_system_on = True
        print("🎮 Gaming system turned ON")
        return "Gaming system: ON"
    
    def turn_off_gaming_system(self):
        """Turn off gaming system."""
        self.gaming_system_on = False
        print("🎮 Gaming system turned OFF")
        return "Gaming system: OFF"
    
    def start_game(self, game):
        """Start playing a specific game."""
        self.current_game = game
        print(f"🎮 Starting game: {game}")
        return f"Playing game: {game}"
    
    def set_movie_mode(self):
        """Set entertainment system to movie mode."""
        print("🎬 Setting movie mode...")
        self.turn_on_tv()
        self.change_channel(1)
        self.set_tv_volume(60)
        self.turn_off_music_system()
        self.turn_off_gaming_system()
        print("🎬 Movie mode activated")
        return "Movie mode: ON"
    
    def set_party_mode(self):
        """Set entertainment system to party mode."""
        print("🎉 Setting party mode...")
        self.turn_on_music_system()
        self.play_music("Party Playlist")
        self.set_music_volume(80)
        self.turn_off_tv()
        self.turn_off_gaming_system()
        print("🎉 Party mode activated")
        return "Party mode: ON"
    
    def set_gaming_mode(self):
        """Set entertainment system to gaming mode."""
        print("🎮 Setting gaming mode...")
        self.turn_on_gaming_system()
        self.start_game("Latest Game")
        self.turn_off_tv()
        self.turn_off_music_system()
        print("🎮 Gaming mode activated")
        return "Gaming mode: ON"
    
    def turn_off_all_entertainment(self):
        """Turn off all entertainment devices."""
        print("🔇 Turning off all entertainment...")
        self.turn_off_tv()
        self.turn_off_music_system()
        self.turn_off_gaming_system()
        print("🔇 All entertainment devices turned OFF")
        return "All entertainment: OFF"
    
    def get_status(self):
        """Get current entertainment status."""
        return {
            'tv': "ON" if self.tv_on else "OFF",
            'tv_channel': self.tv_channel,
            'tv_volume': self.tv_volume,
            'music_system': "ON" if self.music_system_on else "OFF",
            'music_volume': self.music_volume,
            'current_song': self.current_song,
            'gaming_system': "ON" if self.gaming_system_on else "OFF",
            'current_game': self.current_game
        }
