import numpy as np
import pygame
from Graphics import Graphics
from State import State


class Soph:
    def __init__(self, state = None) -> None:
        if state:
            self.state = state

        self.state = self.get_init_state()
        

    def isLeagal(self, state, action): #action --> (first, last)
        first, last = action
        return self.isLeagalFirst(state, first) and self.isLeagalLast(state, last, first)
    
    def isLeagalFirst(self, state , first):
        row, col = first
        if not(row <7 and row >= 0 and col < 8 and col >= 0):
            return False
        if state.player == 1:
            return state.board[row, col] == 1 or state.board[row, col] == 3
        else:
            return state.board[row, col] == 2 or state.board[row, col] == 4


    def get_init_state(self, player= None):
        if player:
            return State([], player) 
           
        return State([], 1) 

    def isLeagalLast(self,state: State,last, first):
        Frow, Fcol = first
        Lrow, Lcol = last
        if not(Lrow <7 and Lrow >= 0 and Lcol <8 and Lcol >= 0):
            return False
        if not(np.abs(Fcol - Lcol) == 1 and np.abs(Frow - Lrow) == 2) and not(np.abs(Fcol - Lcol) == 2 and np.abs(Frow- Lrow) == 1): 
            return False
        if state.board[first] == 3 and state.board[last] != 1:
            return False
        if state.board[first] == 4 and state.board[last] != 2:
            return False
        if state.board[first] == 1 and state.board[last] != 0:
            return False
        if state.board[first] == 2 and state.board[last] != 0:
            return False

        return True
    
    def move(self, state, action):
        first, last = action
        first_row, first_col = first
        last_row, last_col = last
        state.board[first_row, first_col], state.board[last_row, last_col] =  state.board[last_row, last_col], state.board[first_row, first_col]
        state.switchPlayer() 

    def is_end_of_game(self, state: State, action=None):
        Ball1_pos = np.where(state.board == 3)
        Ball2_pos = np.where(state.board == 4)
        if Ball1_pos[1][0] == 7 or Ball2_pos[1][0] == 0:
            return True
        return False

    def get_all_legal_actions (self, state: State) -> list:
        last_add = [(2,1), (2, -1), (1, 2 ), (1, -2 ), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        player = state.player
        pieces = self.get_all_pieces(state, player)
        legal_actions = []
        for first in pieces:
            for add in last_add:
                last = first[0]+add[0], first[1]+add[1]
                action = first,last
                if self.isLeagal(state, action):
                    legal_actions.append(action)
        return legal_actions


    def get_all_pieces(self, state : State, player):
        if player == 1:
            rows, cols = np.where((state.board == 1) | (state.board == 3) )
            pieces = list(zip(rows, cols))
            return pieces
        if player == 2 or player == -1:
            rows, cols = np.where((state.board == 2) | (state.board == 4) )
            pieces = list(zip(rows, cols))
            return pieces
        
    def get_next_state (self, state:State, action):
        next_state = state.copy()
        self.move(next_state, action)
        return next_state

    def end_of_game(self, state: State):
            for i in range(7):
                if state.board[i,7] == 3:
                    return 1
            for i in range(7):
                if state.board[i,0] == 4:
                    return 2
            return 0
    
    def reward (self, state : State, action = None) -> tuple:
        # winner = self.end_of_game(state)
        # if winner == 1:
        #     return 1, True
        # elif winner == 2:
        #     return -1, True
        
        # else:
        #     base, destination = action
        #     if state.board[destination] == 3 and base[1] < destination[1]:
        #         return 0.1, False
        #     if state.board[destination] == 4 and base[1] > destination[1]:
        #         return -0.1, False
        #     return 0, False
        if action:
            next_state = self.get_next_state(state, action)
        else:
            next_state = state
            if (self.end_of_game(next_state)):
                winner = self.end_of_game(state)
                if winner == 1:
                    return 1, True
                elif winner == 2:
                    return -1, True
            else:
                return 0, False

        
    