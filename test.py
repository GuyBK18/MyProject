from Soph import Soph
from State import State
import numpy as np

board = np.array( [[0,0,0,0,0,0,0],
         [0,0,2,0,0,0,0],
         [2,0,0,0,0,0,0],
         [0,0,0,3,0,2,0],
         [0,0,0,0,0,4,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [1,1,0,1,1,2,0]])

state = State(board)
env = Soph()

actions = env.get_all_legal_actions(state)

print(actions)