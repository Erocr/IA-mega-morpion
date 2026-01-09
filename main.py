from Game import *
from AI import *
from MiniMax import MiniMax


game = Game(MiniMax(lambda gs: 0), PlayerAI())
game.play()
