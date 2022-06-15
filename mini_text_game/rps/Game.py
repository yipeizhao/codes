import random
class Game:
    def __init__(self):
        # Defining all valid moves
        self.valid_move = ("rock","paper","scissor")
        self.score = 0
        print("Welcome to the rock paper scissor game")
        self.__main__()

    def __main__(self):
        while True:
            # Ask the player to input a move
            user_move = input("Please choose your move:")
            # If player inputs a invalid move, ask the player to input again
            # Not case sensitive
            user_move = user_move.lower()
            if user_move not in self.valid_move:
                print("You input an invalid command.")
            else:
                # Choose a random bot move
                bot_move = random.choice(self.valid_move)
                print("Bot decided to go for: "+bot_move)
                # Use win_or_lose function to determine win
                res = self.win_or_lose(user_move,bot_move)
                if res == "Win":
                    self.score += 1
                elif res == "Lost":
                    self.score -= 1
                print("The game result is: " + res)
                print("Your current score is: "+str(self.score) + "\n")


    def win_or_lose(self,player_move,bot_move):
        # 1 == player win
        # 0 == player draw
        # -1 == player lost
        if player_move == bot_move:
            return "Draw"
        # Encoding moves
        dic = {"rock":0,"paper":1,"scissor":2}
        # Decided wether the player's move is after the bot or the case is scissor-rock
        return "Win" if (dic[player_move]-dic[bot_move]==1 or dic[player_move]-dic[bot_move]==-2) else "Lost"

if __name__ == "__main__":
    game = Game()
