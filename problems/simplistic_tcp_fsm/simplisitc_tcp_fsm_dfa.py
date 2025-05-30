"""
Simplistic TCP Finite State Machine (DFA-based Solution)

This script solves the Codewars problem "Simplistic TCP Finite State Machine".
The task is to simulate a simplified TCP state machine. Given an initial state and a list of events, determine the final state after processing all events.
The possible states are: CLOSED, LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT, CLOSE_WAIT, LAST_ACK.
The events include actions like APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK.

The solution uses a deterministic finite automaton (DFA) approach, implemented with nested if-statements.
For each state, we check the event and transition to the next state if the event is valid. If the event is invalid, we return "ERROR".

Example:
- State: "CLOSED", Events: ["APP_PASSIVE_OPEN"] -> "LISTEN"
- State: "CLOSED", Events: ["APP_ACTIVE_OPEN"] -> "SYN_SENT"
- State: "LISTEN", Events: ["RCV_SYN"] -> "SYN_RECEIVED"

Time Complexity: O(n), where n is the number of events.
Space Complexity: O(1), as we only use a few variables.
"""

def automate_transition(state: str, events: list) -> str:
    """
    Simulate a TCP state machine using a DFA with nested if-statements.

    Args:
        state (str): The initial state of the TCP connection (e.g., "CLOSED").
        events (list): A list of events to process (e.g., ["APP_PASSIVE_OPEN"]).

    Returns:
        str: The final state after processing all events, or "ERROR" if an invalid transition occurs.
    """
    # Start with the initial state
    current_state = state

    # Process each event in the list
    for event in events:
        # CLOSED state transitions
        if current_state == "CLOSED":
            if event == "APP_PASSIVE_OPEN":
                current_state = "LISTEN"
            elif event == "APP_ACTIVE_OPEN":
                current_state = "SYN_SENT"
            else:
                return "ERROR"

        # LISTEN state transitions
        elif current_state == "LISTEN":
            if event == "RCV_SYN":
                current_state = "SYN_RECEIVED"
            elif event == "APP_SEND":
                current_state = "SYN_SENT"
            elif event == "APP_CLOSE":
                current_state = "CLOSED"
            else:
                return "ERROR"

        # SYN_SENT state transitions
        elif current_state == "SYN_SENT":
            if event == "RCV_SYN":
                current_state = "SYN_RECEIVED"
            elif event == "RCV_SYN_ACK":
                current_state = "ESTABLISHED"
            elif event == "APP_CLOSE":
                current_state = "CLOSED"
            else:
                return "ERROR"

        # SYN_RECEIVED state transitions
        elif current_state == "SYN_RECEIVED":
            if event == "APP_CLOSE":
                current_state = "FIN_WAIT_1"
            elif event == "RCV_ACK":
                current_state = "ESTABLISHED"
            else:
                return "ERROR"

        # ESTABLISHED state transitions
        elif current_state == "ESTABLISHED":
            if event == "APP_CLOSE":
                current_state = "FIN_WAIT_1"
            elif event == "RCV_FIN":
                current_state = "CLOSE_WAIT"
            else:
                return "ERROR"

        # FIN_WAIT_1 state transitions
        elif current_state == "FIN_WAIT_1":
            if event == "RCV_FIN":
                current_state = "CLOSING"
            elif event in ["RCV_FIN_ACK", "RCV_ACK"]:
                current_state = "FIN_WAIT_2"
            else:
                return "ERROR"

        # FIN_WAIT_2 state transitions
        elif current_state == "FIN_WAIT_2":
            if event == "RCV_FIN":
                current_state = "TIME_WAIT"
            else:
                return "ERROR"

        # CLOSING state transitions
        elif current_state == "CLOSING":
            if event == "RCV_ACK":
                current_state = "TIME_WAIT"
            else:
                return "ERROR"

        # TIME_WAIT state transitions
 | current_state == "TIME_WAIT":
            if event == "APP_TIMEOUT":
                current_state = "CLOSED"
            else:
                return "ERROR"

        # CLOSE_WAIT state transitions
        elif current_state == "CLOSE_WAIT":
            if event == "APP_CLOSE":
                current_state = "LAST_ACK"
            else:
                return "ERROR"

        # LAST_ACK state transitions
        elif current_state == "LAST_ACK":
            if event == "RCV_ACK":
                current_state = "CLOSED"
            else:
                return "ERROR"

        # If the current state is not recognized, return "ERROR"
        else:
            return "ERROR"

    # Return the final state after processing all events
    return current_state


if __name__ == "__main__":
    """
    Test the state machine with various scenarios.
    This block runs when the script is executed directly, allowing us to verify the function's behavior.
    """
    # Test cases with expected outputs
    test_cases = [
        (("CLOSED", ["APP_PASSIVE_OPEN"]), "LISTEN"),
        (("CLOSED", ["APP_ACTIVE_OPEN"]), "SYN_SENT"),
        (("LISTEN", ["RCV_SYN"]), "SYN_RECEIVED"),
        (("ESTABLISHED", ["APP_CLOSE", "RCV_FIN"]), "ERROR"),
        (("CLOSED", ["APP_PASSIVE_OPEN", "RCV_SYN", "APP_CLOSE", "RCV_FIN_ACK", "RCV_ACK"]), "FIN_WAIT_2"),
    ]

    # Run each test case and print the result
    for (state, events), expected in test_cases:
        result = automate_transition(state, events)
        print(f"State: {state}, Events: {events} -> Result: {result}, Expected: {expected}")