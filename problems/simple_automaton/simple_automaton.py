class Automaton(object):
    """
    https://www.codewars.com/kata/design-a-simple-automaton-finite-state-machine
    Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

    Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states: q1, q2, and q3. Here is the description of the states:

    q1 is our start state, we begin reading commands from here
    q2 is our accept state, we return true if this is our last state
    And the transitions:

    q1 moves to q2 when given a 1, and stays at q1 when given a 0
    q2 moves to q3 when given a 0, and stays at q2 when given a 1
    q3 moves to q2 when given a 0 or 1

    The automaton should return whether we end in our accepted state (q2), or not (true/false).
    """
    def __init__(self):
        # Dictionary für die Transitionen
        self.states = {
            'q1': {'0': 'q1', '1': 'q2'},
            'q2': {'0': 'q3', '1': 'q2'},
            'q3': {'0': 'q2', '1': 'q2'}
        }
        # Startzustand
        self.current_state = 'q1'

    def read_commands(self, commands):
        # Setze den Zustand auf den Startzustand zurück
        self.current_state = 'q1'

        # Verarbeite jede Eingabe
        for command in commands:
            # Aktualisiere den aktuellen Zustand basierend auf der Eingabe
            self.current_state = self.states[self.current_state][command]

        # Gib True zurück, wenn der Endzustand q2 ist, sonst False
        return self.current_state == 'q2'