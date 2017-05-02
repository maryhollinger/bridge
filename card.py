class Card(object):
	ranks = '23456789TJQKA'
	suits = 'CDHS'

	def __init__(self, string):
		self.rank = string[0]
		self.suit = string[1]

def main():
	test_card = Card('2C')
	print(test_card.rank)
	print(test_card.suit)

if __name__ == "__main__":
  main()