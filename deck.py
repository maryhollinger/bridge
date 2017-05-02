from card import Card

class Deck(object):
	def __init__(self):
		self.cards = []
		for rank in Card.ranks:
			for suit in Card.suits:
				card_string = rank + suit
				print card_string
				self.cards.append(Card(card_string))

def main():
	test_deck = Deck()

if __name__ == "__main__":
  main()