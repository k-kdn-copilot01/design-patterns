# State Pattern - Python Implementation

The **State Pattern** is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

## 🎯 Intent

- Allow an object to alter its behavior when its internal state changes
- The object will appear to change its class
- Encapsulate state-specific behavior and state transitions

## 🏗️ Structure

```
State Pattern Structure:
├── State (Abstract)
│   └── handle_request(context)
├── ConcreteStateA, ConcreteStateB, ConcreteStateC
│   └── handle_request(context) [implements]
└── Context
    ├── _state: State
    ├── set_state(state)
    ├── request()
    └── get_state()
```

## 📁 Files Structure

```
Python/
├── Structure/                    # Basic pattern implementation
│   ├── state.py                 # Abstract State and Context classes
│   ├── concrete_states.py       # Concrete state implementations
│   └── Main.py                  # Structure demo
├── Example/                     # Real-world example
│   ├── audio_player_states.py   # Audio player state classes
│   ├── audio_player.py          # Audio player context
│   └── Main.py                  # Example demo
└── README.md                    # This file
```

## 🚀 How to Run

### Structure Demo (Basic Implementation)

```bash
cd Behavioral/State/Python/Structure
python Main.py
```

**Expected Output:**
```
=== State Pattern Structure Demo ===

1. Creating context with initial state (ConcreteStateA)
   Current state: ConcreteStateA

2. Making requests to demonstrate state transitions:

   Request 1:
Handling request in State A
Transitioning to State B...
State changed to: ConcreteStateB
   Current state: ConcreteStateB

   Request 2:
Handling request in State B
Transitioning to State C...
State changed to: ConcreteStateC
   Current state: ConcreteStateC

   Request 3:
Handling request in State C
Transitioning back to State A...
State changed to: ConcreteStateA
   Current state: ConcreteStateA

   Request 4 (back to State A):
Handling request in State A
Transitioning to State B...
State changed to: ConcreteStateB
   Current state: ConcreteStateB

=== Demo Complete ===
```

### Example Demo (Audio Player)

```bash
cd Behavioral/State/Python/Example
python Main.py
```

**Expected Output:**
```
=== State Pattern - Audio Player Example ===

1. Creating audio player
   Initial state: StoppedState

2. Loading a track
Loaded track: My Favorite Song.mp3

3. Demonstrating state transitions:

   Scenario 1: Start playing from stopped state
   Clicking Play button:
Starting playback...
   Current state: PlayingState

   Scenario 2: Try to play while already playing
   Clicking Play button again:
Already playing. No-op
   Current state: PlayingState

   Scenario 3: Pause the playback
   Clicking Pause button:
Pausing...
   Current state: PausedState

   Scenario 4: Try to pause while already paused
   Clicking Pause button again:
Already paused. No-op
   Current state: PausedState

   Scenario 5: Resume from paused state
   Clicking Play button:
Resuming playback...
   Current state: PlayingState

   Scenario 6: Stop the playback
   Clicking Stop button:
Stopping playback and releasing resources...
   Current state: StoppedState

   Scenario 7: Try to pause when stopped
   Clicking Pause button:
Cannot pause when stopped
   Current state: StoppedState

   Scenario 8: Try to stop when already stopped
   Clicking Stop button:
Already stopped. No-op
   Current state: StoppedState

=== Demo Complete ===
```

## 🔍 Key Components

### 1. State (Abstract Base Class)
- Defines the interface for all concrete states
- Contains abstract methods that concrete states must implement

### 2. Concrete States
- Implement state-specific behavior
- Handle state transitions by changing the context's state
- Each state knows which state to transition to next

### 3. Context
- Maintains a reference to the current state
- Delegates state-specific requests to the current state object
- Provides methods to change state

## 💡 Benefits

1. **Single Responsibility**: Each state class handles behavior for one state
2. **Open/Closed Principle**: Easy to add new states without modifying existing code
3. **Eliminates Conditional Logic**: No need for large if-else or switch statements
4. **State Transitions**: Clear and explicit state transitions
5. **Maintainability**: Easy to understand and modify state-specific behavior

## 🎯 When to Use

- An object's behavior depends on its state
- You have many conditional statements that depend on the object's state
- State-specific behavior changes frequently
- You want to avoid large conditional statements

## 🔄 State Transitions

The State pattern makes state transitions explicit and manageable:

- **Stopped → Playing**: When play button is clicked
- **Playing → Paused**: When pause button is clicked
- **Paused → Playing**: When play button is clicked
- **Playing/Paused → Stopped**: When stop button is clicked

## 📚 Related Patterns

- **Strategy Pattern**: Similar structure but different intent (algorithm selection vs state management)
- **Command Pattern**: Can be used together to encapsulate state transitions
- **Observer Pattern**: Can notify observers when state changes

## 🛠️ Implementation Notes

- States are typically implemented as singletons if they don't maintain state
- Context can store additional data that states might need
- State transitions can be triggered by external events or internal conditions
- Consider using enums for state identification if needed
