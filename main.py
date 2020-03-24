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
        print("Shuffling cards")
        idx = random.randint(1, 53)
        card = self.cards[idx]

        del self.cards[idx]
        self.cards.append(card)

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
    
    print(len(cards))
    print(cards[-1].to_string())

    deck = Deck(cards)
    deck.shuffle()

    print(len(cards))
    print(cards[-1].to_string())


if __name__ == "__main__":
    main()