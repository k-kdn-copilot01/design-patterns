"""
MediaPlayer interface that defines the standard interface for media playback.
"""
from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    """
    The MediaPlayer interface defines the standard interface for media playback
    that our application expects.
    """
    
    @abstractmethod
    def play(self, audio_type: str, filename: str) -> str:
        """
        Play a media file.
        
        Args:
            audio_type: The type of audio (mp3, mp4, vlc, avi)
            filename: The name of the file to play
            
        Returns:
            A string describing the playback result
        """
        pass
