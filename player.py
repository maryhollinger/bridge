from roundy import Round
from hand import Hand
from card import Card

class Player(object):
  """
    Can be human player or AI, acts as bidder
  """

  def __init__(self, isAI, pnum, hand):
    self.AI = isAI
    self.num = num
    self.tricks = [0,0,0,0,0]


  def __str__(self):
    if self.AI:
        h = ''
    else:
        h = 'not '
    print('player number ' + self.num + " is " + h + 'an AI')

  def evalHand(self):
    points = 0
    for c in hand.cards():
        points += c.value()


  def getPBids(self):


