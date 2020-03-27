from deck import new_deck
from hand import new_hand

class Game():
    """
    This class represents the game loop.
    """
    def __init__(self):
        pass

    def play(self):
        print("Starting new game")
        self.deck = new_deck()

        self.player_hand = new_hand([])
        self.dealer_hand = new_hand([])

        self.winner = "Nobody"

        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

        player = True
        while player:
            self.print_hands()
            if self.player_blackjack():
                print("Player has Blackjack!")
                player = False
                self.winner = "Player"
                break
            if self.player_bust():
                print("Player gone bust.")
                player = False
                dealer = False
                self.winner = "Dealer"
                break

            print()
            choice = input("Hit or Stand? ").lower()
            if choice in ["s", "stand"]:
                player = False
            elif choice in ["h", "hit"]:
                self.player_hand.add_card(self.deck.deal_card())

        dealer = True
        print("Dealer's turn.")
        while dealer:
            self.print_hands()
            if self.dealer_blackjack():
                print("Dealer has Blackjack!")
                dealer = False
                break
            if self.dealer_bust():
                dealer = False
                break

            if self.dealer_hand.get_score() < 21:
                self.dealer_hand.add_card(self.deck.deal_card())

        if self.player_blackjack() and self.dealer_blackjack():
            self.winner = "Both"
            self.announce_winner()

        if self.player_bust() and self.dealer_bust():
            self.winner = "Nobody"
            self.announce_winner()

        if self.player_bust() != True and self.dealer_bust():
            self.winner = "Player"
            self.announce_winner()
        if self.dealer_bust() != True and self.player_bust():
            self.winner = "Dealer"
            self.announce_winner()

        if self.player_hand.get_score() > self.dealer_hand.get_score() and self.player_hand.get_score() <= 21:
            self.winner = "Player"
            self.announce_winner()
        elif self.player_hand.get_score() < self.dealer_hand.get_score() and self.dealer_hand.get_score() <= 21:
            self.winner = "Dealer"
            self.announce_winner()
        else:
            self.winner = "Both"
            self.announce_winner()

    def player_blackjack(self):
        return self.player_hand.get_score() == 21

    def dealer_blackjack(self):
        return self.dealer_hand.get_score() == 21

    def player_bust(self):
        return self.player_hand.get_score() > 21

    def dealer_bust(self):
        return self.dealer_hand.get_score() > 21

    def print_hands(self):
        print()
        print("Your Hand: {} => {}".format(self.player_hand.get_score(), self.player_hand.show_hand()))
        print("Dealer's Hand: {} => {}".format(self.dealer_hand.get_score(), self.dealer_hand.show_hand()))

    def announce_winner(self):
        print("The winner is: {}".format(self.winner))
        exit(0)

def new_game():
    return Game()