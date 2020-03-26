import random

from card import Card

SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

class Deck():
    """
    This class represents a generic deck of cards.
    """
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        for idx_a, _ in enumerate(self.cards):
            idx_b = random.randint(0, 51)
            self.cards[idx_a], self.cards[idx_b] = self.cards[idx_b], self.cards[idx_a]

    def get_cards(self):
        return self.cards

    def get_cards_string(self):
        return [c.to_string() for c in self.cards]

    def get_card_values(self):
        return [c.value for c in self.cards]

def new_deck():
    cards = []
    for _, suit in enumerate(SUITS):
        for count, rank in enumerate(RANKS, 1):
            cards.append(Card(count, rank, suit))
    
    deck = Deck(cards)
    deck.shuffle()
    return deck