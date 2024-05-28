import torch
import random
import math
from DQN import DQN
from constant import *
from State import State
from Soph import *
import numpy as np

class DQN_Agent:
    def __init__(self, player = 1, parametes_path = None, train = True, env:Soph= None):
        self.DQN = DQN()
        if parametes_path:
            self.DQN.load_params(parametes_path)
        self.player = player
        self.train = train
        self.setTrainMode()
        self.env = env

    def setTrainMode (self):
          if self.train:
              self.DQN.train()
          else:
              self.DQN.eval()

    def get_Action (self, state:State, epoch = 0, events= None, train = True, graphics = None, black_state = None) -> tuple:
        actions = self.env.get_all_legal_actions(state=state)
        if self.train and train:
            epsilon = self.epsilon_greedy(epoch)
            rnd = random.random()
            if rnd < epsilon:
                return random.choice(actions)
        
        state_tensor= state.toTensor()
        flattend_actions = []
        for action in actions:
            flattend_actions.append((action[0][0], action[0][1],action[1][0],action[1][1]))
        
        action_np = np.array(flattend_actions, dtype=np.float32)
        action_tensor = torch.from_numpy(action_np)
        
        expand_state_tensor = state_tensor.unsqueeze(0).repeat((len(action_tensor),1))
        
        with torch.no_grad():
            Q_values = self.DQN(expand_state_tensor, action_tensor)
        max_index = torch.argmax(Q_values)
        return actions[max_index]

    def get_Actions (self, states_tensor, dones) -> torch.tensor:
        actions = []
        for i, board in enumerate(states_tensor):
            if dones[i].item():
                actions.append(((0,0), (0,0)))
            else:
                state = State.tensorToState(state_tensor=board,player=self.player)
                actions.append(self.get_Action(state, train=False))
        return torch.tensor(actions).reshape(-1,4)

    def epsilon_greedy(self,epoch, start = epsilon_start, final=epsilon_final, decay=epsiln_decay):
        res = final + (start - final) * math.exp(-1 * epoch/decay)
        return res
    
    def loadModel (self, file):
        self.model = torch.load(file)
    
    def save_param (self, path):
        self.DQN.save_params(path)

    def load_params (self, path):
        self.DQN.load_params(path)

    def __call__(self, events= None, state=None):
        return self.get_Action(state)