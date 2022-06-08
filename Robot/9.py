from enum import Enum


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5


class StateMachine:
    state = State.A

    def move(self):
        return self.update({
            State.A: [State.B, 0],
            State.D: [State.B, 6],
            State.B: [State.E, 2],
            State.C: [State.D, 3],
            State.E: [State.C, 8]
        })

    def etch(self):
        return self.update({
            State.B: [State.C, 1],
            State.C: [State.F, 4],
            State.D: [State.E, 5],
            State.E: [State.F, 7]
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal


def main():
    return StateMachine()