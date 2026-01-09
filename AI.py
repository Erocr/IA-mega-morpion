class AI:
    can_be_player2 = None

    def chose_action(self, game_state, actions):
        assert False, "It's an abstract method !!!"


class PlayerAI(AI):
    can_be_player2 = True

    def chose_action(self, game_state, actions):
        print(game_state.draw_game())
        while True:
            s = input("Que jouez vous >>> ")
            try:
                a, b = s.split(" ")
                i = int(a)
                j = int(b)
                res = actions.index((i, j))
                break
            except:
                print("Ceci n'est pas valide")
        return res
