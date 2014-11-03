import math
from Line import Line

N = 100
lr = 0.01

l = Line()


def scalar(V):
  return math.sqrt(V[0]**2+V[1]**2)

def Eout(W, n):
  samples = l.generate_sample(n)
  count = 0.0
  for sample in samples:
    pred = 1 if (W[0]*1 + W[1]*sample[0]) > 0 else -1
    if pred is not sample[1]:
      count += 1
  return count

def learn():
  samples = l.generate_sample(N)

  W = [0, 0]
  w = [99, 99]
  error = [0, 0]
  c = 0
  while(scalar([W[0]-w[0], W[1]-w[1]]) > 0.01):
    c += 1
    for sample in samples:
      x = sample[0]
      X = [1, x]
      y = sample[1]
      e = [(float(y)/(1+math.pow(math.e,y*(W[0]*X[0]+W[1]*X[1])))) * i for i in X]
      error[0] += e[0]
      error[1] += e[1]
    delta_error = [-(1.0/N)*i for i in error]
    w = W
    W[0] = W[0] - lr*delta_error[0]
    W[1] = W[1] - lr*delta_error[1]
  print "C",c
  return W

if __name__ == "__main__":
  l = Line()
  n = 100000
  runs = 1
  eout = 0
  for i in xrange(0,runs):
    l.random_line()
    weight = learn()
    print weight
    eout += Eout(weight, n)
  print eout, float(eout)/(n*runs)
