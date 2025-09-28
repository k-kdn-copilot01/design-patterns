"""
State Pattern - Audio Player Example
Audio player context class that uses the State pattern
"""

from audio_player_states import StoppedState


class AudioPlayer:
    """
    Audio player that uses the State pattern to manage its behavior
    based on its current state (stopped, playing, paused).
    """
    
    def __init__(self):
        """
        Initialize the audio player in stopped state.
        """
        self._state = StoppedState()
        self._current_track = None
    
    def set_state(self, state):
        """
        Change the current state of the player.
        
        Args:
            state: The new state object
        """
        self._state = state
    
    def get_state(self):
        """
        Get the current state of the player.
        
        Returns:
            The current state object
        """
        return self._state
    
    def click_play(self):
        """
        Handle play button click by delegating to current state.
        """
        self._state.click_play(self)
    
    def click_pause(self):
        """
        Handle pause button click by delegating to current state.
        """
        self._state.click_pause(self)
    
    def click_stop(self):
        """
        Handle stop button click by delegating to current state.
        """
        self._state.click_stop(self)
    
    def load_track(self, track_name):
        """
        Load a track for playback.
        
        Args:
            track_name: Name of the track to load
        """
        self._current_track = track_name
        print(f"Loaded track: {track_name}")
    
    def get_current_track(self):
        """
        Get the currently loaded track.
        
        Returns:
            The current track name
        """
        return self._current_track
