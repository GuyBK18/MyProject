import pygame
from Graphics import *
from Soph import Soph
from State import State
MAXSCORE = 1000

class MinMax:
    
    def __init__(self,environment: Soph,player = 1,  depth = 2 )  -> None:
        self.player = player
        if self.player == 1:
            self.opponent = 2
        else:
            self.opponent = 1
        self.depth = depth
        self.environment : Soph = environment
    
    def evaluate (self, state:State):
        
        BALL_VALUE = 2

        
        eof = self.environment.end_of_game(state) 
        if eof == self.player:
            return 500
        elif eof != 0:
            return -500
        
        
        indices_piece = np.where(state.board==1)
        indices_ball = np.where(state.board==3)
        pieces_rows, pieces_cols = indices_piece
        ball_row, ball_col = indices_ball
        white_score=(pieces_cols).sum() + ball_col*10
        white_score = white_score.item()
                
        indices_piece = np.where(state.board==2)
        indices_ball = np.where(state.board==4)
        pieces_rows, pieces_cols = indices_piece
        ball_row, ball_col = indices_ball
        black_score = (7-pieces_cols).sum() + (7-ball_col)*10
        black_score = black_score.item()

        if self.player == 1:
            return white_score - black_score
        else:
            return black_score - white_score

        
    
    def get_Action(self, events = None, graphics = None, state: State = None):
        value, bestAction = self.minMax(state)
        return bestAction

    def minMax(self, state:State):
        visited = set()
        depth = 0
        return self.max_value(state, visited, depth)
        
    def max_value (self, state:State, visited:set, depth):
        
        value = -MAXSCORE

        # stop state
        if depth == self.depth or self.environment.end_of_game(state) != 0:
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_all_legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(state, action)
            # if newState not in visited:
                # visited.add(newState)
            newValue, newAction = self.min_value(newState, visited,  depth + 1)
            if newValue > value:
                    if newValue == 18:
                        x=1
                    value = newValue
                    bestAction = action

        if bestAction == None:
            x=1
        return value, bestAction 

    def min_value (self, state:State, visited:set, depth):
        
        value = MAXSCORE

        # stop state
        if depth == self.depth or self.environment.end_of_game(state) != 0:
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_all_legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(action=action, state=state)
            # if newState not in visited:
                # visited.add(newState)
            newValue, newAction = self.max_value(newState, visited,  depth + 1)
            if newValue < value:
                    value = newValue
                    bestAction = action

        if bestAction == None:
            x=1
        return value, bestAction  
