class Automaton(object):
    """
    https://www.codewars.com/kata/54acc128329e634e9a000362
    The input array of events will consist of one or more of the following strings:

    APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN,
    RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK

    The states are as follows and should be returned in all capital letters as shown:

    CLOSED, LISTEN, SYN_SENT, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK,
    FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT

    The input will be an array of events. The initial state is CLOSED.
    Your job is to traverse the FSM as determined by the events, and return the proper final state
    as a string, all caps, as shown above.

    If an event is not applicable to the current state, your code will return "ERROR".

    Action of each event upon each state:
    (the format is INITIAL_STATE: EVENT -> NEW_STATE)

    CLOSED: APP_PASSIVE_OPEN -> LISTEN
    CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
    LISTEN: RCV_SYN          -> SYN_RCVD
    LISTEN: APP_SEND         -> SYN_SENT
    LISTEN: APP_CLOSE        -> CLOSED
    SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
    SYN_RCVD: RCV_ACK        -> ESTABLISHED
    SYN_SENT: RCV_SYN        -> SYN_RCVD
    SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
    SYN_SENT: APP_CLOSE      -> CLOSED
    ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
    ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
    FIN_WAIT_1: RCV_FIN      -> CLOSING
    FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
    FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
    CLOSING: RCV_ACK         -> TIME_WAIT
    FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
    TIME_WAIT: APP_TIMEOUT   -> CLOSED
    CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
    LAST_ACK: RCV_ACK        -> CLOSED

    ["APP_PASSIVE_OPEN", "APP_SEND", "RCV_SYN_ACK"] =>  "ESTABLISHED"
    ["APP_ACTIVE_OPEN"] =>  "SYN_SENT"
    ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "APP_CLOSE", "RCV_FIN_ACK", "RCV_ACK"] =>  "ERROR"
    """
    def __init__(self):
        # Dictionary für die Transitionen
        self.transitions =  {
                'CLOSED': {
                    'APP_PASSIVE_OPEN': 'LISTEN',
                    'APP_ACTIVE_OPEN': 'SYN_SENT'
                },
                'LISTEN': {
                    'RCV_SYN': 'SYN_RCVD',
                    'APP_SEND': 'SYN_SENT',
                    'APP_CLOSE': 'CLOSED'
                },
                'SYN_RCVD': {
                    'APP_CLOSE': 'FIN_WAIT_1',
                    'RCV_ACK': 'ESTABLISHED'
                },
                'SYN_SENT': {
                    'RCV_SYN': 'SYN_RCVD',
                    'RCV_SYN_ACK': 'ESTABLISHED',
                    'APP_CLOSE': 'CLOSED'
                },
                'ESTABLISHED': {
                    'APP_CLOSE': 'FIN_WAIT_1',
                    'RCV_FIN': 'CLOSE_WAIT'
                },
                'FIN_WAIT_1': {
                    'RCV_FIN': 'CLOSING',
                    'RCV_FIN_ACK': 'TIME_WAIT',
                    'RCV_ACK': 'FIN_WAIT_2'
                },
                'CLOSING': {
                    'RCV_ACK': 'TIME_WAIT'
                },
                'FIN_WAIT_2': {
                    'RCV_FIN': 'TIME_WAIT'
                },
                'TIME_WAIT': {
                    'APP_TIMEOUT': 'CLOSED'
                },
                'CLOSE_WAIT': {
                    'APP_CLOSE': 'LAST_ACK'
                },
                'LAST_ACK': {
                    'RCV_ACK': 'CLOSED'
                }
            }
        # Startzustand
        self.current_state = 'CLOSED'

    def read_commands(self, commands):
        # Setze den Zustand auf den Startzustand zurück
        self.current_state = 'CLOSED'

        # Verarbeite jede Eingabe
        for command in commands:
            # Aktualisiere den aktuellen Zustand basierend auf der Eingabe
            if command not in self.current_state:
                raise ValueError("Invalid command"'{command}' "in current state""'{self.current_state}")
            self.current_state = self.transitions[self.current_state][command]

        # Gib den aktuellen Zustand zurück
        return self.current_state

    class Automaton:
        def __init__(self):
                self.transitions = {
                    'CLOSED': {
                        'APP_PASSIVE_OPEN': 'LISTEN',
                        'APP_ACTIVE_OPEN': 'SYN_SENT'
                    },
                    'LISTEN': {
                        'RCV_SYN': 'SYN_RCVD',
                        'APP_SEND': 'SYN_SENT',
                        'APP_CLOSE': 'CLOSED'
                    },
                    'SYN_RCVD': {
                        'APP_CLOSE': 'FIN_WAIT_1',
                        'RCV_ACK': 'ESTABLISHED'
                    },
                    'SYN_SENT': {
                        'RCV_SYN': 'SYN_RCVD',
                        'RCV_SYN_ACK': 'ESTABLISHED',
                        'APP_CLOSE': 'CLOSED'
                    },
                    'ESTABLISHED': {
                        'APP_CLOSE': 'FIN_WAIT_1',
                        'RCV_FIN': 'CLOSE_WAIT'
                    },
                    'FIN_WAIT_1': {
                        'RCV_FIN': 'CLOSING',
                        'RCV_FIN_ACK': 'TIME_WAIT',
                        'RCV_ACK': 'FIN_WAIT_2'
                    },
                    'CLOSING': {
                        'RCV_ACK': 'TIME_WAIT'
                    },
                    'FIN_WAIT_2': {
                        'RCV_FIN': 'TIME_WAIT'
                    },
                    'TIME_WAIT': {
                        'APP_TIMEOUT': 'CLOSED'
                    },
                    'CLOSE_WAIT': {
                        'APP_CLOSE': 'LAST_ACK'
                    },
                    'LAST_ACK': {
                        'RCV_ACK': 'CLOSED'
                    }
            }
            self.current_state = 'CLOSED'

        def read_commands(self, commands):
            self.current_state = 'CLOSED'
            for command in commands:
                if command not in self.transitions.get(self.current_state, {}):
                    return "ERROR"
                self.current_state = self.transitions[self.current_state][command]
            return self.current_state

    def traverse_TCP_states(events):
        automaton = Automaton()
        return automaton.read_commands(events)