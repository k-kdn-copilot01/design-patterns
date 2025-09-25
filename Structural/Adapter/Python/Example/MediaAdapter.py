"""
MediaAdapter that adapts AdvancedMediaPlayer to MediaPlayer interface.
"""
from MediaPlayer import MediaPlayer
from AdvancedMediaPlayer import AdvancedMediaPlayer
from VlcPlayer import VlcPlayer
from Mp4Player import Mp4Player


class MediaAdapter(MediaPlayer):
    """
    The MediaAdapter makes the AdvancedMediaPlayer interface compatible
    with the MediaPlayer interface.
    """
    
    def __init__(self, audio_type: str):
        """
        Initialize the MediaAdapter with the appropriate player.
        
        Args:
            audio_type: The type of audio format to support
        """
        self.advanced_music_player: AdvancedMediaPlayer = None
        
        if audio_type.lower() == "vlc":
            self.advanced_music_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_music_player = Mp4Player()
    
    def play(self, audio_type: str, filename: str) -> str:
        """
        Play a media file using the appropriate advanced player.
        
        Args:
            audio_type: The type of audio (mp3, mp4, vlc, avi)
            filename: The name of the file to play
            
        Returns:
            A string describing the playback result
        """
        if audio_type.lower() == "vlc":
            return self.advanced_music_player.play_vlc(filename)
        elif audio_type.lower() == "mp4":
            return self.advanced_music_player.play_mp4(filename)
        else:
            return f"MediaAdapter cannot play {audio_type} file: {filename}"
