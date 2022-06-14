import random
from Player import Player
class Card:
    def __init__(self,num,col):
        self.num = num
        self.col = col
        

def card_stack_generator():
    nums = [str(i) for i in range(0,10)]
    nums[0] = "A";nums.append("J");nums.append("Q");nums.append("K");
    # Hearts, diamonds, spades , clubs
    colors = ["H","D","S","C"]
    card_stack = []
    for n in nums:
        for c in colors:
            card_stack.append(c+n)
    return card_stack

# n = numebr of cards draw
def draw_cards(n,card_stack,player):
    for i in range(n):
        card = random.choice(card_stack)
        player.add_card(card)
        card_stack.remove(card)
    return card_stack,player

# n = round number
# players = player list
def one_round(n, players):
    card_stack = card_stack_generator()
    for p in players:
        draw_cards(5, card_stack, p)
    print("Your hand is:");
    print("   1     2     3     4     5 ")  
    print(players[0].cards)
    print("")
    exchange = input("Please select the index of cards that you want to excchange. \n")
    
def __main__():
    print("Welcome to the poker game.")
    print("Here is the rule:")
    print("- You have an opponent")
    print("- Everyone will be given 5 cards, and you can switch any of them once.")
    print("- After the switch, everyone will show their hands and comapre them.")
    name = input("Now please tell me your name. \n")
    round_no = 1;round_max = 10
    players = [Player(name),Player("Alice"),Player("Bob")]
    while round_no < round_max +2:
        one_round(round_no,players)
        
__main__()