class Bid(object):
  """
  Each bid has a suit in {Clubs, Diamonds, Hearts, Spades, NoTrump} and a level
  in range 1-7 inclusive. A pass is "None".
  """
  def __init__(self, string):
    self.level = string[0]
    self.suit = string[1]

  def __str__(self):
    return self.level + '' + self.suit

def main():
  test_bid = Bid('6C')
  print(test_bid.level)
  print(test_bid.suit)
  print(test_bid)

if __name__ == "__main__":
  main()