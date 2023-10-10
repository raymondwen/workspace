
from PokerGame import PokerGame

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    game = PokerGame(num_players)
    game.play()
