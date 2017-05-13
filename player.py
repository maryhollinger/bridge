from roundy import Round
from hand import Hand
from card import Card

class Player(object):
  """
    Can be human player or AI, acts as bidder
  """
  suits = 'CDHSN'

  def __init__(self, isAI, pnum, hnd, rnd):
    self.AI = isAI
    self.num = num
    self.tricks = [0,0,0,0,0]
    self.hand = hnd
    self.points = hnd.points()
    self.round = rnd

  def __str__(self):
    if self.AI:
        h = ''
    else:
        h = 'not '
    print('player number ' + self.num + " is " + h + 'an AI')

  def makeOpeningBid(self):
    if points < 13:
      return None
    if points < 15:
      for s in suits:



  def evalHand(self):
    if

  def getPairBids(self):
    bidsf = round.getBids()
    pairBids = []
    for i in range(len(bidsf)):
      if i % 2 != self.num % 2:
      pairBids.append(bidsf[i])
    return pairBids





