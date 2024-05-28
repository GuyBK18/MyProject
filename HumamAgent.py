import pygame
from Graphics import *
from Soph import Soph

class HumanAgent:

    def __init__(self, env, player = 1, graphics=None) -> None:
        self.player = player
        self.mode = "first"
        self.first = None
        self.last = None
        self.env = env
        self.graphics = graphics
        
    def get_Action (self, events= None, state = None):
        for event in events:  
            
            if event.type == pygame.KEYDOWN:
               print (event)
               if  event.key == pygame.K_ESCAPE:
                    print ("esc")
                    self.mode = "first"
                    return None
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print (event)
                # pygame.time.delay(2)
                print("mouse")
                pos = pygame.mouse.get_pos()
                row_col = self.graphics.calc_row_col(pos)
                if self.mode=="first" :
                    if not self.env.isLeagalFirst(self.env.state, row_col):
                        print ("illegal")
                        return None
                    self.first = row_col
                    print("Player " ,self.player," - " ,self.mode, self.first, self.last)
                    self.mode = "last"
                    return None
                if self.mode == "last":
                    self.last = row_col
                    if not self.env.isLeagalLast(self.env.state, self.last, self.first):
                        print ("illegal")
                        return None
                    self.mode="first"
                    action = self.first, self.last
                    print("Player " ,self.player," - " ,self.mode, self.first, self.last)
                    self.first, self.last = None, None
                    return action       
            
        return None
            
    

