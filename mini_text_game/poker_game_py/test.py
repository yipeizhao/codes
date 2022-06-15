import unittest
from Player import Player
import Hand_ranks
import Util

player= Player("test")
f = open("test.txt","w")
class Test(unittest.TestCase):
    def test_hand_ranks(self):
        for i in range(1000):
            cards = Util.card_stack_generator()
            Util.draw_cards(5,cards,player)
            self.assertIsNotNone(Hand_ranks.hand_ranks(player.get_cards()))
            f.write(str(player.get_cards()));f.write("   ");f.write(Hand_ranks.hand_ranks(player.get_cards()));f.write("\n")
            player.clear_hand()
        f.close()
if __name__ == "__main__":
    unittest.main()