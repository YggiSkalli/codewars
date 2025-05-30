"""
Simplistic TCP Finite State Machine (Dictionary-based Solution)

This script solves the Codewars problem "Simplistic TCP Finite State Machine".
The task is to simulate a simplified TCP state machine. Given an initial state and a list of events, determine the final state after processing all events.
The possible states are: CLOSED, LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT, CLOSE_WAIT, LAST_ACK.
The events include actions like APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK.

The solution uses a dictionary to define valid state transitions. For each event, we look up the current state in the dictionary and transition to the new state if the event is valid.
If an event is invalid for the current state, the state remains unchanged. If the transition leads to an "ERROR" state, we return "ERROR".

Example:
- State: "CLOSED", Events: ["APP_PASSIVE_OPEN"] -> "LISTEN"
- State: "CLOSED", Events: ["APP_ACTIVE_OPEN"] -> "SYN_SENT"
- State: "LISTEN", Events: ["RCV_SYN"] -> "SYN_RECEIVED"

Time Complexity: O(n), where n is the number of events.
Space Complexity: O(1), as the dictionary of transitions is fixed in size.
"""

def automate_transition(state: str, events: list) -> str:
    """
    Simulate a TCP state machine using a dictionary of transitions.

    Args:
        state (str): The initial state of the TCP connection (e.g., "CLOSED").
        events (list): A list of events to process (e.g., ["APP_PASSIVE_OPEN"]).

    Returns:
        str: The final state after processing all events, or "ERROR" if an invalid transition occurs.
    """
    # Dictionary mapping (current_state, event) to the next_state
    # If a transition is invalid, it maps to "ERROR"
    transitions = {
        ("CLOSED", "APP_PASSIVE_OPEN"): "LISTEN",
        ("CLOSED", "APP_ACTIVE_OPEN"): "SYN_SENT",
        ("LISTEN", "RCV_SYN"): "SYN_RECEIVED",
        ("LISTEN", "APP_SEND"): "SYN_SENT",
        ("LISTEN", "APP_CLOSE"): "CLOSED",
        ("SYN_SENT", "RCV_SYN"): "SYN_RECEIVED",
        ("SYN_SENT", "RCV_SYN_ACK"): "ESTABLISHED",
        ("SYN_SENT", "APP_CLOSE"): "CLOSED",
        ("SYN_RECEIVED", "APP_CLOSE"): "FIN_WAIT_1",
        ("SYN_RECEIVED", "RCV_ACK"): "ESTABLISHED",
        ("ESTABLISHED", "APP_CLOSE"): "FIN_WAIT_1",
        ("ESTABLISHED", "RCV_FIN"): "CLOSE_WAIT",
        ("FIN_WAIT_1", "RCV_FIN"): "CLOSING",
        ("FIN_WAIT_1", "RCV_FIN_ACK"): "FIN_WAIT_2",
        ("FIN_WAIT_1", "RCV_ACK"): "FIN_WAIT_2",
        ("CLOSING", "RCV_ACK"): "TIME_WAIT",
        ("FIN_WAIT_2", "RCV_FIN"): "TIME_WAIT",
        ("TIME_WAIT", "APP_TIMEOUT"): "CLOSED",
        ("CLOSE_WAIT", "APP_CLOSE"): "LAST_ACK",
        ("LAST_ACK", "RCV_ACK"): "CLOSED",
    }

    # Start with the initial state
    current_state = state

    # Process each event in the list
    for event in events:
        # Look up the transition in the dictionary using the current state and event
        # If the (current_state, event) pair is not in the dictionary, transition to "ERROR"
        next_state = transitions.get((current_state, event), "ERROR")

        # If the transition leads to "ERROR", return "ERROR" immediately
        if next_state == "ERROR":
            return "ERROR"

        # Otherwise, update the current state to the next state
        current_state = next_state

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