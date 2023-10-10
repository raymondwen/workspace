from CardDeck import CardDeck
from Player import Player


class PokerGame:
    def __init__(self, num_players=2):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.card_deck = CardDeck(ranks)
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.pot = 0  # Initialize the pot size to 0

    def display_hand(self, hand):
        for card in hand:
            print(f"{card['rank']}{card['suit']}", end=' ')
        print()

    def display_game_info(self):
        print(f"\nPot: {self.pot} BB")
        for player in self.players:
            print(f"{player.name}: {player.stack} BB")

    def play(self):
        while True:
            play_again = input("Do you want to play a hand of poker? (yes/no): ").lower()

            if play_again != "yes":
                break

            self.card_deck.shuffle()

            for player in self.players:
                player.hand = self.card_deck.deal(2)

            for player in self.players:
                print(f"\n{player.name}'s Hole Cards:", end=' ')
                self.display_hand(player.hand)

            # Pre-flop betting
            current_bet = 0

            while True:
                self.display_game_info()
                for player in self.players:
                    player_bet = player.bet(current_bet)
                    current_bet = player_bet
                    self.pot += player_bet  # Add the player's bet to the pot
                if all(player.stack == 0 for player in self.players) or current_bet == 0:
                    break

            # Flop
            community_cards = self.card_deck.deal(3)
            print("\nFlop:", end=' ')
            self.display_hand(community_cards)

            # Flop betting
            current_bet = 0

            while True:
                self.display_game_info()
                for player in self.players:
                    player_bet = player.bet(current_bet)
                    current_bet = player_bet
                    self.pot += player_bet
                if all(player.stack == 0 for player in self.players) or current_bet == 0:
                    break

            # Turn
            community_cards += self.card_deck.deal(1)
            print("\nTurn:", end=' ')
            self.display_hand(community_cards)

            # Turn betting
            current_bet = 0

            while True:
                self.display_game_info()
                for player in self.players:
                    player_bet = player.bet(current_bet)
                    current_bet = player_bet
                    self.pot += player_bet
                if all(player.stack == 0 for player in self.players) or current_bet == 0:
                    break

            # River
            community_cards += self.card_deck.deal(1)
            print("\nRiver:", end=' ')
            self.display_hand(community_cards)

            # River betting
            current_bet = 0

            while True:
                self.display_game_info()
                for player in self.players:
                    player_bet = player.bet(current_bet)
                    current_bet = player_bet
                    self.pot += player_bet
                if all(player.stack == 0 for player in self.players) or current_bet == 0:
                    break

            # Evaluate hands and store the ranking
            for player in self.players:
                player.rank = self.card_deck.evaluate_hand(player.hand, community_cards, self.card_deck.ranks)
                print(f"\n{player.name}'s Hand Rank:", player.rank[0])

            winning_players = [self.players[0]]

            for player in self.players[1:]:
                if player.rank[1] > winning_players[0].rank[1]:
                    winning_players = [player]
                elif player.rank[1] == winning_players[0].rank[1]:
                    winning_players.append(player)

            if len(winning_players) == 1:
                print(f"\n{winning_players[0].name} wins the hand with {winning_players[0].rank[0]}!")
                winning_players[0].stack += self.pot  # Add the pot to the winning player's stack
            else:
                print("\nIt's a tie!")

            # Show each player's remaining stack and reset the pot
            for player in self.players:
                print(f"{player.name}'s stack: {player.stack} BB")
                player.rank = None  # Reset the player's rank
            self.pot = 0  # Reset the pot

        print("Thanks for playing!")
