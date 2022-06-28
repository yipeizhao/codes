from Hand_ranks import hand_ranks
class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.cards = []
        self.hand =[]
    def get_name(self):
        return self.name
    def add_score(self,n):
        self.score += n
    def clear_hand(self):
        self.cards =[]
    def add_card(self,card):
        self.cards.append(card)
    def remove_card(self,card):
        self.cards.remove(card)
    def get_cards(self):
        return self.cards
    def set_hand_rank(self):
        self.hand = hand_ranks(self.cards)
    def get_hand_rank(self):
        return self.hand