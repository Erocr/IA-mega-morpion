class UtilityFunctions:
    @staticmethod
    def useless(game_state):
        return 0

    @staticmethod
    def win_lose_utility(game_state):
        return game_state.get_winner()

    @staticmethod
    def number_little_games_won(game_state):
        w = game_state.get_winner()
        if w != 0:
            return w * 100
        res = 0
        for e in game_state.table:
            if e == 1:
                res += 1
            elif e == -1:
                res -= 1
        return res

