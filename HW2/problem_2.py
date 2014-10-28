import random
import matplotlib.pyplot as plt

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

  min_d = {}
  first_d = {}
  rand_d = {}

  iterations = 1000
  for i in xrange(0, iterations):
    m, f, r = sample()
    min += m
    first += f
    rand += r
    min_d[m] = (min_d[m]+1 if m in min_d else 0)
    first_d[f] = (first_d[f]+1 if f in first_d else 0)
    rand_d[r] = (rand_d[r]+1 if r in rand_d else 0)
  print "Average Vmin  :", float(min)/(iterations * 10)
  print "Average V1    :", float(first)/(iterations * 10)
  print "Average Vrand :", float(rand)/(iterations * 10)

  plt.plot([key for key in first_d], [float(first_d[key])/iterations for key in first_d])
  plt.plot([key for key in min_d], [float(min_d[key])/iterations for key in min_d])
  plt.plot([key for key in rand_d], [float(rand_d[key])/iterations for key in rand_d])
  plt.show()
  #print min_d, first_d, rand_d
