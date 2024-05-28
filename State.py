import numpy as np
import torch

class State:
    def __init__(self, board = {}, player = 1):
        if  len(board) > 0:
              self.board = board # np.array
        else:
            self.board = self.init_board()
        self.rows, self.cols = self.board.shape
        self.player = player

    def __hash__(self) -> int:
        return hash(repr(self.board))
    
    def score(self, env):
        score = env.end_of_game(env.state)

        if score == 2:
            return -1
        
        return score

    def init_board (self):
       return np.array([[0, 0, 0, 0, 0, 0, 0, 0], 
                         [1, 0, 0 , 0, 0, 0, 0, 2], 
                         [1, 0, 0, 0, 0, 0, 0, 2], 
                         [3, 0, 0, 0, 0, 0, 0, 4], 
                         [1, 0, 0, 0, 0, 0, 0, 2], 
                         [1, 0, 0, 0, 0, 0, 0, 2], 
                         [0, 0, 0, 0, 0, 0, 0, 0]])
        # return np.array([[0, 0, 0, 0, 0, 0, 0, 0], 
        #                  [0, 0, 3 , 0, 0, 0, 0, 0], 
        #                  [0, 0, 1, 0, 0, 0, 0, 2], 
        #                  [0, 0, 1, 0, 0, 0, 0, 4], 
        #                  [0, 0, 0, 0, 0, 0, 0, 0], 
        #                  [0, 0, 0, 0, 0, 0, 0, 0], 
        #                  [0, 0, 0, 0, 0, 0, 0, 0]])

    def get_blank_pos (self):
        pos = np.where(self.board == 0)
        row = pos[0].item()
        col = pos[1].item()
        return row, col

    def switchPlayer (self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def __eq__(self, other):
        return np.equal(self.board, other.board).all()

    def copy (self):
        newBoard = np.copy(self.board)
        return State (newBoard, self.player)

    def getcols(self):
        return self.cols

    def getrows(self):
        return self.rows
            
    def __hash__(self) -> int:
        return hash(repr(self.board))
    
    def reverse (self):
        reversed = self.copy()
        reversed.board[reversed.board == 3] = 30
        reversed.board[reversed.board == 1] = 10
        reversed.board[reversed.board == 2] = 20
        reversed.board[reversed.board == 4] = 40

        reversed.board[reversed.board == 30] = 4
        reversed.board[reversed.board == 40] = 3
        reversed.board[reversed.board == 10] = 2
        reversed.board[reversed.board == 20] = 1
        reversed.player = reversed.player * -1
        return reversed

    def toTensor (self, device = torch.device('cpu')) -> tuple:
        board_np = self.board.reshape(-1)
        board_tensor = torch.tensor(board_np, dtype=torch.float32, device=device)
        return board_tensor
    
    [staticmethod]
    def tensorToState (state_tensor, player):
        board = state_tensor.reshape([7,8]).cpu().numpy()
        return State(board, player=player)