import numpy as np
import pygame
from Graphics import Graphics
from constant import *
from State import State
from HumamAgent import HumanAgent
from MinMax import MinMax
from AlphaBeta import AlphaBeta
import time
from Soph import Soph
from DQN_Agent import DQN_Agent
from Random_Agent import Random_Agent


state = State()
env = Soph(state)
win = pygame.display.set_mode((820, 720))
graphics = Graphics(win)

player1 = HumanAgent(env, player=1, graphics=graphics)  
# player1 = MinMax(env, player=1, depth=3)  
#player1 = Random_Agent(env, player=1) 
# player1 = AlphaBeta(env, player=1, depth=4)
#player1=DQN_Agent(env=env, player=1, train= False, parametes_path="Data/params_3.pth")   
  
#player2 = HumanAgent(env, player=2, graphics=graphics)  
player2 = Random_Agent(env, player=2)
# player2 = AlphaBeta(env, player=2, depth=4) 
#player2 = MinMax(env, player=2, depth=3)
#player2=DQN_Agent(env=env, player=2, train= False, parametes_path="Data/params_115.pth")   
  
def main ():
    count = 0
    player = player1
    FPS = 60
    
    
    run = True
    clock = pygame.time.Clock()
    #graphics.draw(state)
    pygame.display.update()

    while(run):

        clock.tick(FPS)
        count +=1
        if count > 39:
            x=1
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False
        
        action = player.get_Action(state=env.state, events=events)
        if action:
            print (action)
            # print(Soph.isLeagalFirst(Soph.state, action))
            env.move(env.state, action)
            #pygame.time.delay(200)
            
            if env.is_end_of_game(env.state, action):
                print (player.player, "Win")
                run = False
            player = switchPlayer(player)
        
        graphics.draw(env.state)
        
        pygame.display.update()
        # pygame.time.delay(800)

    pygame.quit()

def switchPlayer (player):
    # env.state.switchPlayer() # to delete when changing state
    if player == player1:
        return player2
    else:
        return player1

if __name__ == '__main__':
    main()
    