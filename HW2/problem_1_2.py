import random

def sample():
  coins = []
  min_head = 99
  min_coin = 9999

  for coin in xrange(0,1000):
    heads = 0
    for iteration in xrange(0,10):
      heads += random.randrange(0,2)
    coins.append(heads)
    if heads < min_head:
      min_head = heads
      min_coin = coin
  return float(min_head), float(coins[0]), float(coins[random.randrange(0,1000)])


if __name__ == "__main__":
  min = 0
  first = 0
  rand = 0

  for i in xrange(0, 100000):
    m, f, r = sample()
    min += m
    first += f
    rand += r

  print "Average Vmin  :", float(min)/100000
  print "Average V1    :", float(first)/100000
  print "Average Vrand :", float(rand)/100000
