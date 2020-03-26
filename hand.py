class Hand():
    """
    This class represents a generic hand of card(s).
    Should be sub-classed for specific games.
    """
    def __init__(self, cards):
        self.cards = cards

    def get_score(self):
        total = 0
        for _, card in enumerate(self.cards):
            total += card.value
        return total
    
    def add_card(self, card):
        self.cards.append(card)

def new_hand(cards):
    return Hand(cards)