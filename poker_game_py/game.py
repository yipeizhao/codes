class Card:
    def __init__(self,num,col):
        self.num = num
        self.col = col

class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0
    def add_score(self,n):
        self.score += n
        

def __main__():
	print("Welcome to the poker game.")
	print("Here is the rule:")
	print("- You have an opponent")
	print("- Everyone will be given 5 cards, and you can switch any of them once.")
	print("- After the switch, everyone will show their hands and comapre them.")

def card_stack_generator():
    nums = [str(i) for i in range(0,10)]
    nums[0] = "A";nums.append("J");nums.append("Q");nums.append("K");
    # Hearts, diamonds, spades , clubs
    colors = ["H","D","S","C"]



__main__()