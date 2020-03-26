import unittest

from card import new_card

class TestCard(unittest.TestCase):
    def test_is_available_init(self):
        card = new_card(1, "Ace", "Spades")
        self.assertEqual(card.is_available(), True, "Should be available when initialized.")

    def test_mark_unavailable(self):
        card = new_card(1, "Ace", "Spades")
        card.mark_unavailable()
        self.assertEqual(card.is_available(), False, "Should be unavailable.")

    def test_mark_available(self):
        card = new_card(1, "Ace", "Spades")
        card.mark_available()
        self.assertEqual(card.is_available(), True, "Should be available.")


if __name__ == '__main__':
    unittest.main()
