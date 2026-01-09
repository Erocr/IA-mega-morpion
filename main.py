from Game import *
from AI import *
from MiniMax import MiniMax
from utility_functions import UtilityFunctions


game = Game(MiniMax(UtilityFunctions.number_little_games_won), PlayerAI())
game.play()
