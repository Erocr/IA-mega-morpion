import random


class AI:
    can_be_player2 = None

    def chose_action(self, game_state, actions):
        assert False, "It's an abstract method !!!"


class PlayerAI(AI):
    can_be_player2 = True

    def chose_action(self, game_state, actions):
        print(game_state.draw_game())
        print(game_state.playablePos)
        while True:
            s = input("Que jouez vous >>> ")
            try:
                if len(s) == 2: a, b = s[0], s[1]
                else: a, b = s.split(" ")
                i = int(a.strip())
                j = int(b.strip())
                res = actions.index((i, j))
                break
            except:
                print("Ceci n'est pas valide")
        return res


class RandomAI(AI):
    can_be_player2 = True

    def chose_action(self, game_state, actions):
        return random.randint(0, len(actions)-1)
