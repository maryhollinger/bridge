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

	# def __iter__(self):
 #        return self

 #    def next(self): # Python 3: def __next__(self)
 #        if self.current > self.high:
 #            raise StopIteration
 #        else:
 #            self.current += 1
 #            return self.current - 1


	def cards(self):
		return self.cards

	def points(self):
		val = 0
		for card in self.cards:
			val += card.value()
		return val

	def numSuitPoints(self, suit):
		val = 0
		for card in self.cards:
			if (card.suit == suit):
				val += card.value()
		return val

	def numSuitCards(self, suit):
		val = 0
		for card in self.cards:
			if (card.suit == suit):
				val += 1
		return val

	def getSuitCards(self, suit):
		suitCards = []
		for card in self.cards:
			if (card.suit == suit):
				suitCards.append(card)
		return suitCards

	def numDoubletons(self):
		val = 0
		cCount = 0
		dCount = 0
		hCount = 0
		sCount = 0
		for card in self.cards:
			if (card.suit == 'C'):
				cCount += 1
			elif (card.suit == 'D'):
				dCount += 1
			elif (card.suit == 'H'):
				hCount += 1
			else:
				sCount += 1
		if (cCount == 2):
			val += 1
		if (dCount == 2):
			val += 1
		if (hCount == 2):
			val += 1
		if (sCount == 2):
			val += 1
		return val

	def numSingletons(self):
		val = 0
		cCount = 0
		dCount = 0
		hCount = 0
		sCount = 0
		for card in self.cards:
			if (card.suit == 'C'):
				cCount += 1
			elif (card.suit == 'D'):
				dCount += 1
			elif (card.suit == 'H'):
				hCount += 1
			else:
				sCount += 1
		if (cCount == 1):
			val += 1
		if (dCount == 1):
			val += 1
		if (hCount == 1):
			val += 1
		if (sCount == 1):
			val += 1
		return val

	def numVoids(self):
		val = 0
		cCount = 0
		dCount = 0
		hCount = 0
		sCount = 0
		for card in self.cards:
			if (card.suit == 'C'):
				cCount += 1
			elif (card.suit == 'D'):
				dCount += 1
			elif (card.suit == 'H'):
				hCount += 1
			else:
				sCount += 1
		if (cCount == 0):
			val += 1
		if (dCount == 0):
			val += 1
		if (hCount == 0):
			val += 1
		if (sCount == 0):
			val += 1
		return val

	def isBalanced(self):
		voids = self.numVoids()
		singletons = self.numSingletons()
		doubletons = self.numDoubletons()
		return (voids == 0) and (singletons == 0) and (doubletons <= 1)



def main():
	print('A OK')

if __name__ == "__main__":
  main()