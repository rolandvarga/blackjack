import unittest

from deck import new_deck

class TestDeck(unittest.TestCase):
    def test_deal_card_ok(self):
        deck = new_deck()
        for _ in range(3):
            deck.deal_card()

        self.assertEqual(deck.remaining_cards(), 49, "Should be 49 cards left.")

    def test_deal_card_no_card_left(self):
        deck = new_deck()
        for _ in range(52):
            card = deck.deal_card()

        card = deck.deal_card()
        self.assertEqual(card, None, "Shouldn't receive card.")

    def test_deal_hand(self):
        deck = new_deck()
        hand = deck.deal_hand(5)

        self.assertEqual(len(hand), 5, "Should receive 5 cards.")

    def test_deal_hand_not_enough_cards(self):
        deck = new_deck()
        for _ in range(52):
            card = deck.deal_card()

        hand = deck.deal_hand(3)
        self.assertEqual(hand, [None, None, None], "Shouldn't receive hand.")

    def test_remaining_cards_init_ok(self):
        deck = new_deck()
        count = deck.remaining_cards()

        self.assertEqual(count, 52, "Should be 52 cards at start.")

    def test_remaining_cards_remaining_ok(self):
        deck = new_deck()
        deck.deal_hand(10)
        count = deck.remaining_cards()

        self.assertEqual(count, 42, "Should be 42 cards left.")

    def test_get_cards_ok(self):
        deck = new_deck()
        cards = deck.get_cards()

        self.assertEqual(len(cards), 52, "Should return 52 cards.")

if __name__ == '__main__':
    unittest.main()
