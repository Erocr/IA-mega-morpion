from AI import AI
from MiniMaxTree import MiniMaxTree
import random


class MiniMax(AI):
    can_be_player2 = False

    def __init__(self, utility_func):
        """
        :param utility_func: function of the format: utility(game_state) -> float
        is greater if the situation seem favorable for the player1
        """
        self.utility_func = utility_func
        self.tree = MiniMaxTree(0, None)
        self.visited_game_states = {}

    def create_tree(self, game_state, root, max_depth=2):
        assert max_depth >= 0, "create_tree ne devrait pas descendre aller ausssi loin"
        childs = root.get_childs()
        if len(childs) != 0:
            if max_depth > 0:
                for child in childs:
                    self.create_tree(child.game_state, child, max_depth-1)

        actions = game_state.get_actions()
        for action in actions:
            next_state = game_state.play_action(*action)
            h = next_state.get_hash()
            if h in self.visited_game_states:
                root.add_child(self.visited_game_states[h])
            else:
                value = self.utility_func(next_state)
                next_node = MiniMaxTree(value, next_state)
                root.add_child(next_node)
                self.visited_game_states[next_state.get_hash()] = next_node
                if max_depth > 0:
                    self.create_tree(next_state, next_node, max_depth-1)

    def chose_action(self, game_state, actions):
        self.create_tree(game_state, self.tree)
        values = []
        childs = self.tree.get_childs()
        for i in range(len(actions)):
            values.append(childs[i].get_value(False))
        v = max(values)
        possible_results = []
        for i in range(len(values)):
            if values[i] == v:
                possible_results.append(i)
        res = random.choice(possible_results)
        self.tree = childs[res]
        return res

