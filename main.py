import random

SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

class Deck():
    """
    This class represents a deck of cards.
    """
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        for idx_a, _ in enumerate(self.cards):
            idx_b = random.randint(0, 51)
            self.cards[idx_a], self.cards[idx_b] = self.cards[idx_b], self.cards[idx_a]

    def get_cards(self):
        return ["{} of {}".format(c.rank, c.suit) for c in self.cards]

    def get_card_values(self):
        return [c.value for c in self.cards]

class Card():
    def __init__(self, value, rank, suit):
        self.value = value
        self.rank = rank
        self.suit = suit

    def to_string(self):
        """
        Returns a string representing the current Card.
        """
        return "{} {} of {}".format(self.value, self.rank, self.suit)

def main():
    cards = []
    for _, suit in enumerate(SUITS):
        for count, rank in enumerate(RANKS, 1):
            cards.append(Card(count, rank, suit))
    
    deck = Deck(cards)
    deck.shuffle()

    print(deck.get_cards())


if __name__ == "__main__":
    main()