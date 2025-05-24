class Automaton(object):
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