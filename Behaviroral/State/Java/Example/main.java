// State interface: defines common behaviors
interface ATMState {
    void insertCard();     // Insert a card
    void ejectCard();      // Eject a card
    void withdrawMoney();  // Withdraw money
}

// Concrete State: "No Card" state
class NoCard implements ATMState {
    private ATMMachine atm;   // reference to the Context (ATM machine)

    public NoCard(ATMMachine atm) {
        this.atm = atm;
    }

    public void insertCard() {
        System.out.println("Card has been inserted.");
        atm.setState(atm.getHasCardState()); // switch state to "Has Card"
    }

    public void ejectCard() {
        System.out.println("No card to eject.");
    }

    public void withdrawMoney() {
        System.out.println("Please insert a card first.");
    }
}

// Concrete State: "Has Card" state
class HasCard implements ATMState {
    private ATMMachine atm;

    public HasCard(ATMMachine atm) {
        this.atm = atm;
    }

    public void insertCard() {
        System.out.println("A card is already inserted."); // cannot insert another card
    }

    public void ejectCard() {
        System.out.println("Card has been ejected.");
        atm.setState(atm.getNoCardState()); // switch back to "No Card" state
    }

    public void withdrawMoney() {
        System.out.println("Withdrawal successful!");
        atm.setState(atm.getNoCardState()); // after withdrawal → back to "No Card" state
    }
}

// Context: ATM Machine, manages current state
class ATMMachine {
    private ATMState noCard;       // "No Card" state
    private ATMState hasCard;      // "Has Card" state
    private ATMState currentState; // current state

    public ATMMachine() {
        noCard = new NoCard(this);
        hasCard = new HasCard(this);
        currentState = noCard;  // default state is "No Card"
    }

    // Allows changing the state
    public void setState(ATMState state) {
        currentState = state;
    }

    // Getters for states, used by concrete states
    public ATMState getNoCardState() {
        return noCard;
    }

    public ATMState getHasCardState() {
        return hasCard;
    }

    // Actions delegated to the current state
    public void insertCard() {
        currentState.insertCard();
    }

    public void ejectCard() {
        currentState.ejectCard();
    }

    public void withdrawMoney() {
        currentState.withdrawMoney();
    }
}

// Demo using State Pattern
public class Main {
    public static void main(String[] args) {
        ATMMachine atm = new ATMMachine();

        atm.withdrawMoney();   // no card inserted → prompt to insert
        atm.insertCard();      // insert card → change state to "Has Card"
        atm.insertCard();      // try inserting again → error message
        atm.withdrawMoney();   // withdraw money → success → back to "No Card"
        atm.ejectCard();       // no card to eject → error message
    }
}
