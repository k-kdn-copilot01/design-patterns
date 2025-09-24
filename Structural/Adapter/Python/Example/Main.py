"""
Main demo for Adapter pattern real-world example.
Demonstrates a media player system that can play different audio formats.
"""

from MediaPlayer import MediaPlayer
from AudioPlayer import AudioPlayer
from MediaAdapter import MediaAdapter


def demonstrate_media_player():
    """
    Demonstrate the Adapter pattern with a real-world media player example.
    """
    print("=== Adapter Pattern Demo: Media Player System ===\n")
    
    # Create the main audio player
    audio_player = AudioPlayer()
    
    # Test different audio formats
    test_files = [
        ("mp3", "song.mp3"),
        ("mp4", "movie.mp4"),
        ("vlc", "video.vlc"),
        ("avi", "clip.avi")
    ]
    
    print("1. Testing AudioPlayer (basic implementation):")
    for audio_type, filename in test_files:
        result = audio_player.play(audio_type, filename)
        print(f"   {audio_type.upper()}: {result}")
    print()
    
    print("2. Testing MediaAdapter (advanced formats):")
    # Create adapters for advanced formats
    vlc_adapter = MediaAdapter("vlc")
    mp4_adapter = MediaAdapter("mp4")
    
    # Test VLC files
    print("   VLC Adapter:")
    vlc_result = vlc_adapter.play("vlc", "video.vlc")
    print(f"   {vlc_result}")
    
    # Test MP4 files
    print("   MP4 Adapter:")
    mp4_result = mp4_adapter.play("mp4", "movie.mp4")
    print(f"   {mp4_result}")
    print()
    
    print("3. Testing unsupported formats with adapters:")
    unsupported_result = vlc_adapter.play("avi", "clip.avi")
    print(f"   AVI with VLC Adapter: {unsupported_result}")
    print()
    
    print("4. Demonstrating independent adapter instances:")
    vlc_adapter2 = MediaAdapter("vlc")
    mp4_adapter2 = MediaAdapter("mp4")
    
    print(f"   vlc_adapter == vlc_adapter2: {vlc_adapter is vlc_adapter2}")
    print(f"   mp4_adapter == mp4_adapter2: {mp4_adapter is mp4_adapter2}")
    print(f"   Both adapters work independently:")
    print(f"   Adapter 1 VLC: {vlc_adapter.play('vlc', 'test1.vlc')}")
    print(f"   Adapter 2 VLC: {vlc_adapter2.play('vlc', 'test2.vlc')}")
    print()
    
    print("=== Demo Complete ===")


if __name__ == "__main__":
    demonstrate_media_player()
