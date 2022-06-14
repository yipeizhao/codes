class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.cards = []
    def add_score(self,n):
        self.score += n
    def clear_hand(self):
        self.cards =[]
    def add_card(self,card):
        self.cards.append(card)