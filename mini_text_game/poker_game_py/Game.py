from Player import Player
import Util
import random
name_list = ["Alice","Bob","Charlie","Danny","Elles","Franda","Gabi","Hermes","Illy","Jack","Lanny","Manny","Nancy","Olly","Penny","Quelle","Randy","Sandy","Tilly","Ully","Vicky","Willy","Xavier","Yvonne","Zoe"]
def __main__(round_max = 10,player_num = 3):
    # Greet and ask for the players name
    name = Util.greeting()
    round_no = 1

    # Choosing players' name randomly
    if name in name_list:
        name_list.remove(name)
    players = random.sample(name_list,player_num)
    players = [Player(item) for item in players]
    players.append(Player(name))

    # Increment round within round_max
    while round_no < round_max +2:
        print("Round "+str(round_no))
        Util.one_round(round_no,players)
        round_no+=1

__main__()