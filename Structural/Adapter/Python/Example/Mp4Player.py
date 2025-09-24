"""
Mp4Player implementation of AdvancedMediaPlayer.
"""
from AdvancedMediaPlayer import AdvancedMediaPlayer


class Mp4Player(AdvancedMediaPlayer):
    """
    Concrete implementation of AdvancedMediaPlayer for MP4 files.
    """
    
    def play_vlc(self, filename: str) -> str:
        """
        Mp4Player cannot play VLC files directly.
        
        Args:
            filename: The name of the VLC file (ignored)
            
        Returns:
            A string indicating the file cannot be played
        """
        return f"Mp4Player cannot play vlc file: {filename}"
    
    def play_mp4(self, filename: str) -> str:
        """
        Play an MP4 file.
        
        Args:
            filename: The name of the MP4 file to play
            
        Returns:
            A string describing the playback result
        """
        return f"Playing mp4 file. Name: {filename}"
