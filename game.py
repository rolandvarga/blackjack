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

        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

        player = True
        while player:
            print()
            print("Your Hand: {} => {}".format(self.player_hand.get_score(), self.player_hand.show_hand()))
            print("Dealer's Hand: {} => {}".format(self.dealer_hand.get_score(), self.dealer_hand.show_hand()))
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
        while dealer:
            print()
            print("Dealer's turn.")
            if self.dealer_blackjack():
                print("Dealer has Blackjack!")
                dealer = False
                break
            if self.dealer_bust():
                dealer = False
                break

            if self.dealer_hand.get_score() < 21:
                self.dealer_hand.add_card(self.deck.deal_card())
        
        if self.player_blackjack() & self.dealer_blackjack():
            self.winner = "Both"
        
        if self.player_bust() != True & self.dealer_bust() != True:
            if self.player_hand.get_score() > self.dealer_hand.get_score():
                self.winner = "Player"
            elif self.player_hand.get_score() < self.dealer_hand.get_score():
                self.winner = "Dealer"
            else:
                self.winner = "Both"

        
        print("The winner is: {}".format(self.winner))

    def player_blackjack(self):
        return self.player_hand.get_score() == 21

    def dealer_blackjack(self):
        return self.dealer_hand.get_score() == 21

    def player_bust(self):
        return self.player_hand.get_score() > 21

    def dealer_bust(self):
        return self.dealer_hand.get_score() > 21

def new_game():
    return Game()