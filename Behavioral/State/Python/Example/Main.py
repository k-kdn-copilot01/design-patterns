"""
State Pattern - Audio Player Example Demo
Demonstrates the State pattern with a real-world audio player example
"""

from audio_player import AudioPlayer


def main():
    """
    Main function to demonstrate the State pattern with audio player.
    """
    print("=== State Pattern - Audio Player Example ===\n")
    
    # Create audio player
    print("1. Creating audio player")
    player = AudioPlayer()
    print(f"   Initial state: {type(player.get_state()).__name__}\n")
    
    # Load a track
    print("2. Loading a track")
    player.load_track("My Favorite Song.mp3")
    print()
    
    # Demonstrate state transitions
    print("3. Demonstrating state transitions:")
    
    print("\n   Scenario 1: Start playing from stopped state")
    print("   Clicking Play button:")
    player.click_play()
    print(f"   Current state: {type(player.get_state()).__name__}")
    
    print("\n   Scenario 2: Try to play while already playing")
    print("   Clicking Play button again:")
    player.click_play()
    print(f"   Current state: {type(player.get_state()).__name__}")
    
    print("\n   Scenario 3: Pause the playback")
    print("   Clicking Pause button:")
    player.click_pause()
    print(f"   Current state: {type(player.get_state()).__name__}")
    
    print("\n   Scenario 4: Try to pause while already paused")
    print("   Clicking Pause button again:")
    player.click_pause()
    print(f"   Current state: {type(player.get_state()).__name__}")
    
    print("\n   Scenario 5: Resume from paused state")
    print("   Clicking Play button:")
    player.click_play()
    print(f"   Current state: {type(player.get_state()).__name__}")
    
    print("\n   Scenario 6: Stop the playback")
    print("   Clicking Stop button:")
    player.click_stop()
    print(f"   Current state: {type(player.get_state()).__name__}")
    
    print("\n   Scenario 7: Try to pause when stopped")
    print("   Clicking Pause button:")
    player.click_pause()
    print(f"   Current state: {type(player.get_state()).__name__}")
    
    print("\n   Scenario 8: Try to stop when already stopped")
    print("   Clicking Stop button:")
    player.click_stop()
    print(f"   Current state: {type(player.get_state()).__name__}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
