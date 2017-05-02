class Card(object):
	"""
	Represents a single playing card with 2-letters 'rank' + 'suit'.
	"""
	
	ranks = '23456789TJQKA'
	suits = 'CDHS'

	def __init__(self, string):
		self.rank = string[0]
		self.suit = string[1]

	def __str__(self):
		return self.rank + '' + self.suit

	def value(self):
		if (self.rank == 'A'):
			return 4
		elif (self.rank == 'K'):
			return 3
		elif (self.rank == 'Q'):
			return 2
		elif (self.rank == 'J'):
			return 1
		else:
			return 0

def main():
	test_card = Card('KC')
	print(test_card.rank)
	print(test_card.suit)
	print(test_card)
	print(test_card.value())

if __name__ == "__main__":
  main()