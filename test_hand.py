import unittest

from deck import Deck, new_deck
from hand import Hand, new_hand

class TestHand(unittest.TestCase):
    def test_total_score_ok(self):
        deck = new_deck()
        hand = new_hand(deck.get_cards())

        # total value for a deck with 52 cards == 364
        self.assertEqual(hand.get_score(), 364, "Score should be 364")

if __name__ == '__main__':
    unittest.main()
