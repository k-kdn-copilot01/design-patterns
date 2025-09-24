"""
AudioPlayer implementation of MediaPlayer for basic audio formats.
"""
from MediaPlayer import MediaPlayer


class AudioPlayer(MediaPlayer):
    """
    Concrete implementation of MediaPlayer for basic audio formats.
    """
    
    def play(self, audio_type: str, filename: str) -> str:
        """
        Play a basic audio file (mp3).
        
        Args:
            audio_type: The type of audio (mp3, mp4, vlc, avi)
            filename: The name of the file to play
            
        Returns:
            A string describing the playback result
        """
        if audio_type.lower() == "mp3":
            return f"Playing mp3 file. Name: {filename}"
        elif audio_type.lower() in ["mp4", "vlc", "avi"]:
            return f"AudioPlayer cannot play {audio_type} file: {filename}"
        else:
            return f"Invalid media. {audio_type} format not supported"
