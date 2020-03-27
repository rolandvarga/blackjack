import unittest

from deck import new_deck
from card import Card
from hand import new_hand

class TestHand(unittest.TestCase):
    def test_total_score_ok(self):
        deck = new_deck()
        hand = new_hand(deck.get_cards())

        # total value for a deck with 52 cards == 364
        self.assertEqual(hand.get_score(), 364, "Score should be 364")

    def test_add_card(self):
        cards = [Card(1, "Ace", "Spades"), Card(13, "King", "Hearts")]
        hand = new_hand(cards)
        hand.add_card(Card(11, "Jack", "Diamonds"))

        self.assertEqual(len(hand.cards), 3, "Should be 3 cards")


if __name__ == '__main__':
    unittest.main()
