from deck import Deck
from hand import Hand

def main():
	test_deck = Deck()
	print test_deck
	test_deck.shuffle()
	print test_deck

	hand_1 = test_deck.cards[0:13]
	p1 = Hand(hand_1)
	print 'Player 1:'
	print str(p1) + ' val=' + str(p1.value())

	hand_2 = test_deck.cards[13:26]
	p2 = Hand(hand_2)
	print 'Player 2:'
	print str(p2) + ' val=' + str(p2.value())

	hand_3 = test_deck.cards[26:39]
	p3 = Hand(hand_3)
	print 'Player 3:'
	print str(p3) + ' val=' + str(p3.value())

	hand_4 = test_deck.cards[39:52]
	p4 = Hand(hand_4)
	print 'Player 4:'
	print str(p4) + ' val=' + str(p4.value())

if __name__ == "__main__":
  main()