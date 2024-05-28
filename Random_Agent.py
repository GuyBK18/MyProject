from Soph import Soph
import random

class Random_Agent:

    def __init__(self, env:Soph, player) -> None:
        self.player = player
        self.env = env

    def get_Action (self, state = None, events=None):
        legal_Actions = self.env.get_all_legal_actions(state)
        for action in legal_Actions:
            if state.board[action[0]] == 3 and action[0][1] < action[1][1]:
                return action
            if state.board[action[0]] == 4 and action[0][1] > action[1][1]:
                return action

        return random.choice(legal_Actions)