from Player import Player
import Util
import random
name_list = ["Alice","Bob","Charlie","Danny","Elles","Franda","Gabi","Hermes","Illy","Jack","Lanny"]
def __main__():
    name = Util.greeting()
    round_no = 1;round_max = 3
    if name in name_list:
        name_list.remove(name)
        
    players = random.sample(name_list,2)
    players = [Player(item) for item in players]
    players.append(Player(name))
    while round_no < round_max +2:
        print("Round "+str(round_no))
        Util.one_round(round_no,players)
        round_no+=1
        
    for p in players:
        p.clear_hand()
    
__main__()