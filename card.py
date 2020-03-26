class Card():
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

    def to_string(self):
        """
        Returns a string representing the current Card.
        """
        return "{} {} of {}".format(self.value, self.rank, self.suit)