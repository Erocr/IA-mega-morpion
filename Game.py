from GameState import *


class PlayerVsPlayer:
    def __init__(self):
        self.game_state = GameState()
        self.actions = self.game_state.get_actions()

    def draw_game(self):
        for i in range(9):
            for j in range(9):
                big_line = i // 3
                big_col = j // 3
                big_pos = big_col + big_line * 3
                small_line = i % 3
                small_col = j % 3
                if self.game_state.table[big_pos] == 1:
                    if small_line == small_col == 1:
                        print("X", end="")
                    if (small_col, small_line) == (0, 0) or (small_col, small_line) == (2, 2):
                        print("\\", end="")
                    if (small_col, small_line) == (2, 0) or (small_col, small_line) == (0, 2):
                        print("/", end="")
                elif self.game_state.table[big_pos] == -1:
                    """
                    .-.
                    | |
                    '-'
                    """
                    if small_line == small_col == 1:
                        print(" ", end="")
                    if (small_col, small_line) == (0, 0) or (small_col, small_line) == (2, 0):
                        print(".", end="")
                    if (small_col, small_line) == (0, 2) or (small_col, small_line) == (2, 2):
                        print("'", end="")
                    if (small_col, small_line) == (1, 0) or (small_col, small_line) == (1, 2):
                        print("-", end="")
                    if (small_col, small_line) == (0, 1) or (small_col, small_line) == (2, 1):
                        print("|", end="")
                else:
                    small_pos = small_col + small_line * 3
                    if self.game_state.table[big_pos][small_pos] == 1:
                        print("X", end="")
                    elif self.game_state.table[big_pos][small_pos] == -1:
                        print("O", end="")
                    else:
                        print(".", end="")
                if j % 3 == 2:
                    print("|", end="")
            print("")
            if i % 3 == 2:
                print("---|---|---|")

    def get_actions(self):
        return self.actions

    def play(self, i):
        self.game_state = self.game_state.play_action(*self.actions[i])
        self.actions = self.game_state.get_actions()
