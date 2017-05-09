from card import Card
import random

class Deck(object):
	"""
	Represents a 52-card deck of cards, initialized in order from least valuable
	to most valuable (2-Ace, Clubs, Diamonds, Hearts, then Spades).
	"""

	def __init__(self):
		self.cards = []
		for rank in Card.ranks:
			for suit in Card.suits:
				card_string = rank + suit
				self.cards.append(Card(card_string))

	def __str__(self):
		deck_string = '[ '
		for card in self.cards:
			deck_string += str(card) + ', '
		deck_string += ']'
		return deck_string

	def shuffle(self):
		random.shuffle(self.cards)

def main():
	test_deck = Deck()
	print test_deck
	test_deck.shuffle()
	print test_deck

if __name__ == "__main__":
  main()