from GameState import *
from AI import AI


class Game:
    def __init__(self, player1: AI, player2: AI):
        assert player2.can_be_player2, "On ne peut pas placer le joueur 2 comme joueur 2"
        self.game_state = GameState()
        self.p1 = player1
        self.p2 = player2
        self.actions = self.game_state.get_actions()

    def play(self):
        winner = 0
        while winner == 0:
            self.__play()
            winner = self.game_state.get_winner()
        print(f"!!!!!!!!  The winner is {winner}  !!!!!!!!!")

    def __play(self):
        if self.game_state.currentPlayer == 1:
            i = self.p1.chose_action(self.game_state, self.actions)
        else:
            i = self.p2.chose_action(self.game_state, self.actions)
        self.game_state = self.game_state.play_action(*self.game_state.get_actions()[i])
        self.actions = self.game_state.get_actions()
