from Gamev2 import Game
from bots import *

game = Game(width=5, respawn_prob=0.1)
while not game.terminate:
    output = game.output()
    command = basic_bot(*output)
    game.display()
    print(command)
    game.movement(command)
game.display()