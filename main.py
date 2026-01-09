from Game import *


game = PlayerVsPlayer()
while True:
    game.draw_game()
    print(game.actions)
    i = int(input())
    game.play(i)
