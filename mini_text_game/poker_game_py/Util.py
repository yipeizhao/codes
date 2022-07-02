import random
import Hand_ranks

# Greeting the player
# Para:
    # None
# Return:
    # name = player's name
def greeting():
    print("Welcome to the poker game.")
    print("Here is the rule:")
    print("- You have an opponent")
    print("- Everyone will be given 5 cards, and you can switch any of them once.")
    print("- After the switch, everyone will show their hands and comapre them.")
    name = input("Now please tell me your name. \n")
    return name

# Returns a clean card stack
# Para:
    # None
# Return:
    # card_stack = clean card stack
def card_stack_generator():
    nums = [str(i) for i in range(1,11)]
    nums[0] = "A";nums.append("J");nums.append("Q");nums.append("K");
    # Hearts, diamonds, spades , clubs
    suits = ["H","D","S","C"]
    card_stack = []
    for n in nums:
        for c in suits:
            card_stack.append(c+n)
    return card_stack

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
        player.draw_cards(card_stack,len(index))
        return player.get_cards()
    
# n = round number
# players = player list
# return the result of the game
def one_round(n, players):
    card_stack = card_stack_generator()
    for p in players:
        p.draw_cards(card_stack,5)
    print("Your hand is:");
    print("   1     2     3     4     5 ")  
    print(players[0].get_cards())
    print("")
    print("Please select the index of cards that you want to exchange, seperated by space. \n")
    index = input("If you don't want to exchange any card, input 0. \n")

    # The game will only continue with a valid input
    flag = True
    while flag:
        # Exchange will return None if an invalid input is entered
        if exchange(players[0], index, card_stack) == None:
            index = input("You entered an invalid command. Please try again.")
        else:
            flag = False
    # Command all players to set their hand ranks
    for p in players:
        p.set_hand_rank()
    # Sort the players by their hand ranks
    res = Hand_ranks.sort_hand(players)
    for i in range(len(res)):
        print("Rank   " + str(i+1) + "   " + res[i].get_name() + "   [" +  (",").join(res[i].get_cards()) + "]   "+ res[i].get_hand_rank()[-1])
    _ = input("Press enter to continue \n")
    for item in players:
        item.clear_hand()   
        