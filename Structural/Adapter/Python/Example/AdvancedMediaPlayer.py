"""
AdvancedMediaPlayer interface for advanced media formats.
"""
from abc import ABC, abstractmethod


class AdvancedMediaPlayer(ABC):
    """
    The AdvancedMediaPlayer interface for playing advanced media formats.
    """
    
    @abstractmethod
    def play_vlc(self, filename: str) -> str:
        """
        Play a VLC file.
        
        Args:
            filename: The name of the VLC file to play
            
        Returns:
            A string describing the playback result
        """
        pass
    
    @abstractmethod
    def play_mp4(self, filename: str) -> str:
        """
        Play an MP4 file.
        
        Args:
            filename: The name of the MP4 file to play
            
        Returns:
            A string describing the playback result
        """
        pass
