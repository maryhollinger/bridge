from bid import Bid

class Round(object):
  """
  Each round of bidding is a list of bids
  """
  bidsuits = 'CDHSN'
  def __init__(self):
    self.bids = []

  def __str__(self):
    round_string = '[ '
    for bid in self.bids:
      round_string += str(bid) + ', '
    round_string += ']'
    return round_string

  def nextPlayer(self):
    return len(self.bids)%4 + 1


  def addBid(self, newbid):
    if self.bids:
      #self.bids non-empty
      prebid = self.bids[-1]
      if(newbid.level < prebid.level):
        raise ValueError('Invalid Bid')
      if(newbid.level == prebid.level and Round.bidsuits.index(newbid.suit)
        <= Round.bidsuits.index(prebid.suit)):
        raise ValueError('Invalid Bid')
    print('adding bid: ' + str(newbid))
    self.bids.append(newbid)

  def getBids(self):
    return self.bids


def main():
  test_round = Round()
  print(test_round.nextPlayer())
  test_round.addBid(Bid('1H'))
  print(test_round.nextPlayer())
  test_round.addBid(Bid('2S'))
  print(test_round.nextPlayer())
  test_round.addBid(Bid('3H'))
  try:
    test_round.addBid(Bid('3C'))
    raise Exception
  except ValueError as e:
    print e
  print(test_round.nextPlayer())
  test_round.addBid(Bid('4H'))
  print(test_round.nextPlayer())
  test_round.addBid(Bid('5N'))
  print(test_round.nextPlayer())
  try:
    test_round.addBid(Bid('1H'))
    raise Exception
  except ValueError as e:
    print e
  try:
    test_round.addBid(Bid('5C'))
    raise Exception
  except ValueError as e:
    print e
  try:
    test_round.addBid(Bid('5N'))
    raise Exception
  except ValueError as e:
    print e
  print(test_round)

if __name__ == "__main__":
  main()