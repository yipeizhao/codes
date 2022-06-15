from Player import Player
import Util

def __main__():
    name = Util.greeting()
    round_no = 1;round_max = 10
    players = [Player(name),Player("Alice"),Player("Bob")]
    while round_no < round_max +2:
        Util.one_round(round_no,players)

__main__()