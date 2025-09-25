"""
VlcPlayer implementation of AdvancedMediaPlayer.
"""
from AdvancedMediaPlayer import AdvancedMediaPlayer


class VlcPlayer(AdvancedMediaPlayer):
    """
    Concrete implementation of AdvancedMediaPlayer for VLC files.
    """
    
    def play_vlc(self, filename: str) -> str:
        """
        Play a VLC file.
        
        Args:
            filename: The name of the VLC file to play
            
        Returns:
            A string describing the playback result
        """
        return f"Playing vlc file. Name: {filename}"
    
    def play_mp4(self, filename: str) -> str:
        """
        VlcPlayer cannot play MP4 files directly.
        
        Args:
            filename: The name of the MP4 file (ignored)
            
        Returns:
            A string indicating the file cannot be played
        """
        return f"VlcPlayer cannot play mp4 file: {filename}"
