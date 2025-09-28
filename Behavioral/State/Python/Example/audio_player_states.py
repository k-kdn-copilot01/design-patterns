"""
State Pattern - Audio Player Example
Real-world implementation of State pattern for an audio player
"""

from abc import ABC, abstractmethod


class PlayerState(ABC):
    """
    Abstract base class for audio player states.
    """
    
    @abstractmethod
    def click_play(self, player):
        """Handle play button click"""
        pass
    
    @abstractmethod
    def click_pause(self, player):
        """Handle pause button click"""
        pass
    
    @abstractmethod
    def click_stop(self, player):
        """Handle stop button click"""
        pass


class StoppedState(PlayerState):
    """
    State when the audio player is stopped.
    """
    
    def click_play(self, player):
        print("Starting playback...")
        player.set_state(PlayingState())
    
    def click_pause(self, player):
        print("Cannot pause when stopped")
    
    def click_stop(self, player):
        print("Already stopped. No-op")


class PlayingState(PlayerState):
    """
    State when the audio player is playing.
    """
    
    def click_play(self, player):
        print("Already playing. No-op")
    
    def click_pause(self, player):
        print("Pausing...")
        player.set_state(PausedState())
    
    def click_stop(self, player):
        print("Stopping playback and releasing resources...")
        player.set_state(StoppedState())


class PausedState(PlayerState):
    """
    State when the audio player is paused.
    """
    
    def click_play(self, player):
        print("Resuming playback...")
        player.set_state(PlayingState())
    
    def click_pause(self, player):
        print("Already paused. No-op")
    
    def click_stop(self, player):
        print("Stopping playback and releasing resources...")
        player.set_state(StoppedState())
