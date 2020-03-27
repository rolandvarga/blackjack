class Card():
    """
    This is the class representation of a Card.
    Should be sub-classed for specific games.
    """
    def __init__(self, value, rank, suit):
        self.value = value
        self.rank = rank
        self.suit = suit
        self.available = True
    
    def is_available(self):
        return self.available
    
    def mark_unavailable(self):
        self.available = False
    
    def mark_available(self):
        self.available = True
    
    def show_card(self):
        return "{} of {}".format(self.rank, self.suit)

    def to_string(self):
        return "|{}| {} of {}".format(self.value, self.rank, self.suit)

def new_card(value, rank, suit):
    return Card(value, rank, suit)