from Random_Agent import Random_Agent
from DQN_Agent import DQN_Agent
from Soph import Soph
from State import State
from MinMax import MinMax

class Tester:
    def __init__(self, env:Soph, player1, player2) -> None:
        self.env = env
        self.player1 = player1
        self.player2 = player2
        

    def test (self, games_num):
        env = self.env
        temp = State()
        player = self.player1
        env.state = State(temp.init_board(), player.player)
        player1_win = 0
        player2_win = 0
        games = 0
        while games < games_num:
            action = player.get_Action(state=env.state)
            env.move(action=action, state=env.state)
            player = self.switchPlayers(player)
            if env.is_end_of_game(env.state):
                score = env.state.score(env)
                if score > 0:
                    player1_win += 1

                elif score < 0:
                    player2_win += 1

                env.state = env.get_init_state(player.player)
                games += 1
                player = self.player1
        return player1_win, player2_win        

    def switchPlayers(self, player):
        if player == self.player1:
            return self.player2
        else:
            return self.player1

    def __call__(self, games_num):
        return self.test(games_num)

if __name__ == '__main__':
    env = Soph()
    player1 = DQN_Agent(env=env, player=1, parametes_path=f'Data/params_201.pth')
    #player1 = Random_Agent(env, player=1)
    #player1 = MinMax(env, player=1, depth=3)
    player2 = Random_Agent(env, player=-1)
    #player2 = DQN_Agent(env=env, player=-1, parametes_path=f'Data/params_115.pth')
    test = Tester(env, player1 ,player2)
    print(test.test(100))