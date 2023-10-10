class Player:
    def __init__(self, name, starting_stack=100):
        self.name = name
        self.hand = []
        self.stack = starting_stack  # Start with the specified starting stack
        self.rank = None  # Store the hand ranking

    def bet(self, current_bet):
        while True:
            try:
                bet_amount = int(input(f"{self.name}, your stack is {self.stack} BB. Enter your bet amount: "))
                if bet_amount >= current_bet and bet_amount <= self.stack:
                    self.stack -= bet_amount  # Update the player's stack after the bet
                    return bet_amount
                else:
                    print("Bet amount should be equal to or greater than the current bet and less than or equal to your stack.")
            except ValueError:
                print("Invalid input. Please enter a valid bet amount.")
