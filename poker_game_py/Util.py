import random

def greeting():
    print("Welcome to the poker game.")
    print("Here is the rule:")
    print("- You have an opponent")
    print("- Everyone will be given 5 cards, and you can switch any of them once.")
    print("- After the switch, everyone will show their hands and comapre them.")
    name = input("Now please tell me your name. \n")
    return name

# Returns a clean card stack
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
# Returns the current card stack and the player
def draw_cards(n,card_stack,player):
    for i in range(n):
        # Draw a random card
        card = random.choice(card_stack)
        # Add the random card to the players hand
        player.add_card(card)
        # Remove the card from the stack
        card_stack.remove(card)
    return card_stack,player

# Exchange a players current hand with given index
# Return player's current hand
def exchange(player,index,card_stack):
    # If the player doesnt want to exchange
    if index == "0":
        return player.get_cards()
    # An invalid command is entered, a string contains letter except:
    # space or 12345
    if set(index)|set(" 12345") != set(" 12345"):
        return None
    else:
        # Find all index
        index = set(index)
        if " " in index:
            index.remove(" ")
        # Remove cards from player's hand
        remove_cards = [player.get_cards()[int(i)-1] for i in index]
        for item in remove_cards:
            player.remove_card(item)
        # Draw equivalent cards
        draw_cards(len(index), card_stack, player)
        return player.get_cards()
    
# n = round number
# players = player list
def one_round(n, players):
    card_stack = card_stack_generator()
    for p in players:
        draw_cards(5, card_stack, p)
    flag = True
    print("Your hand is:");
    print("   1     2     3     4     5 ")  
    print(players[0].get_cards())
    print("")
    print("Please select the index of cards that you want to exchange, seperated by space. \n")
    index = input("If you don't want to exchange any card, input 0. \n")
    flag = True
    while flag:
        if exchange(players[0], index, card_stack) == None:
            index = input("You entered an invalid command. Please try again.")
        else:
            flag = False
            new_hand = players[0].get_cards()