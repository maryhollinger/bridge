from card import Card

class Hand(object):
	"""
	Represents a 13-card starting hand to be used for bidding.
	"""

	def __init__(self, cards):
		self.cards = cards

	def __str__(self):
		hand_string = '[ '
		for card in self.cards:
			hand_string += str(card) + ', '
		hand_string += ']'
		return hand_string

	def points(self):
		val = 0
		for card in self.cards:
			val += card.value()
		return val

def main():
	print('A OK')

if __name__ == "__main__":
  main()