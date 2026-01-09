from copy import deepcopy


class GameState:
    def __init__(self, table=None, currentPlayer=1, playablePosition=-1):
        """
        :param table:
        The table is a list, with each little tic-tac-toe game.
        If no one won the little tic-tac-toe, it is the state of the little tic-tac-toe, on the format of a list.
        0 for empty, 1 for the player1, -1 for player2.
        If someone won the little tic-tac-toe, we put 1, or -1 instead.
        :param currentPlayer:
        1 for player1, -1 for player2
        :param playablePosition:
        the position where the current player can play
        -1 if he can play anywhere

        The default parameters are for the initial state
        """
        assert playablePosition == -1 or isinstance(table[playablePosition], list), "pfff, bug de merde"
        if table is None:
            table = [[0 for _ in range(9)] for _ in range(9)]
        self.table = table
        self.currentPlayer = currentPlayer
        self.playablePos = playablePosition

    @staticmethod
    def find_mini_win(table):
        hors1 = [0, 0, 0]
        vers1 = [0, 0, 0]
        hors2 = [0, 0, 0]
        vers2 = [0, 0, 0]
        for i in range(3):
            for j in range(3):
                if table[i*3+j] == 1:
                    hors1[i] += 1
                    vers1[j] += 1
                if table[i*3+j] == -1:
                    hors2[i] += 1
                    vers2[j] += 1
        diag1 = diag2 = antidiag1 = antidiag2 = 0
        for i in range(3):
            if table[i*3+i] == 1: diag1 += 1
            if table[i*3+i] == -1: diag2 += 1
            if table[i*3+2 - i] == 1: antidiag1 += 1
            if table[i*3+2 - i] == -1: antidiag2 += 1
        if diag1 == 3 or hors1[0] == 3 or hors1[1] == 3 or hors1[2] == 3\
                or vers1[0] == 3 or vers1[1] == 3 or vers1[2] == 3:
            return 1
        if diag2 == 3 or hors2[0] == 3 or hors2[1] == 3 or hors2[2] == 3\
                or vers2[0] == 3 or vers2[1] == 3 or vers2[2] == 3:
            return -1
        else:
            return 0

    def get_winner(self):
        return self.find_mini_win(self.table)

    def get_actions(self):
        # Actions are tuples: (bigPos, smallPos)
        if self.playablePos == -1:
            res = []
            for bigPos in range(len(self.table)):
                if isinstance(self.table[bigPos], list):
                    for smallPos in range(len(self.table[bigPos])):
                        if self.table[bigPos][smallPos] == 0:
                            res.append((bigPos, smallPos))
            return res
        else:
            res = []
            for smallPos in range(len(self.table[self.playablePos])):
                if self.table[self.playablePos][smallPos] == 0:
                    res.append((self.playablePos, smallPos))
            return res

    def play_action(self, bigPos, smallPos):
        new_table = deepcopy(self.table)
        new_table[bigPos][smallPos] = self.currentPlayer
        mini_win = self.find_mini_win(new_table[bigPos])
        if 0 not in new_table[bigPos]:
            new_table[bigPos] = 0
        elif mini_win != 0:
            new_table[bigPos] = mini_win
        new_current_player = -self.currentPlayer
        if isinstance(new_table[smallPos], list):
            new_playable_pos = smallPos
        else:
            new_playable_pos = -1
        return GameState(new_table, new_current_player, new_playable_pos)

    def draw_game(self):
        for i in range(9):
            for j in range(9):
                big_line = i // 3
                big_col = j // 3
                big_pos = big_col + big_line * 3
                small_line = i % 3
                small_col = j % 3
                if self.table[big_pos] == 1:
                    if small_line == small_col == 1:
                        print("X", end="")
                    elif (small_col, small_line) == (0, 0) or (small_col, small_line) == (2, 2):
                        print("\\", end="")
                    elif (small_col, small_line) == (2, 0) or (small_col, small_line) == (0, 2):
                        print("/", end="")
                    else:
                        print(" ", end="")
                elif self.table[big_pos] == -1:
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
                    if self.table[big_pos][small_pos] == 1:
                        print("X", end="")
                    elif self.table[big_pos][small_pos] == -1:
                        print("O", end="")
                    else:
                        print(".", end="")
                if j % 3 == 2:
                    print("|", end="")
            print("")
            if i % 3 == 2:
                print("---|---|---|")

    def get_hash(self):
        res = ""
        for i in range(9):
            if isinstance(self.table[i], list):
                for j in range(9):
                    if self.table[i][j] == 0:
                        res += "0"
                    elif self.table[i][j] == 1:
                        res += "1"
                    else:
                        res += "2"
            elif self.table[i] == 1:
                res += "1"*9
            else:
                res += "2"*9
        return int(res, 3) * self.currentPlayer

