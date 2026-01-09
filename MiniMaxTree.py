class MiniMaxTree:
    def __init__(self, value, game_state):
        self.value = value
        self.game_state = game_state
        self.childs = []

    def add_child(self, node):
        self.childs.append(node)

    def get_childs(self):
        return self.childs

    def get_value(self, isPlaying):
        if len(self.childs) == 0:
            return self.value
        else:
            child_values = []
            for child in self.childs:
                child_values.append(child.get_value(not isPlaying))
            if isPlaying:
                return max(child_values)
            else:
                return min(child_values)

