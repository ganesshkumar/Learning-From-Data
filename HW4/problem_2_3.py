import matplotlib.pyplot as plt
import math

Dvc = 50
delta = 0.05
epsilon1 = 1
epsilon2 = 1

# problem 2
n = 10000
n_reduced = 1000

# problem 3
#n = 5
#n_reduced = 5

def original_vs_bound(N):
  return math.sqrt((8*math.log((4*math.pow(2*N,Dvc))/delta)/N))

def rademacher_penalty_bound(N):
  return math.sqrt((2*math.log(2*math.pow(2*N,Dvc)))/N) + math.sqrt((2/N)*(math.log(1/delta))) + (1/N)

def parrondo_and_van_den_broek(N):
  global epsilon1
  epsilon1 = math.sqrt((float(1)/N)*(2*epsilon1 + math.log((6*math.pow(2*N,Dvc))/delta)))
  return epsilon1

def devroye(N):
  global epsilon2
  epsilon2 = math.sqrt((float(1)/(2*N))*(4*epsilon2*(1+epsilon2) + math.log(4*math.pow(N**2,Dvc)/delta)))
  return epsilon2

plt.plot([i for i in xrange(1,n+1)], [ original_vs_bound(i) for i in xrange(1,n+1)], 'yellow')
plt.plot([i for i in xrange(1,n+1)], [ rademacher_penalty_bound(i) for i in xrange(1,n+1)], 'green')
plt.plot([i for i in xrange(1,n+1)], [ parrondo_and_van_den_broek(i) for i in xrange(1,n+1)], 'blue')
plt.plot([i for i in xrange(1,n_reduced+1)], [ devroye(i) for i in xrange(1,n_reduced+1)], 'red')
plt.axis([0, n, 0, 1]) # Comment this our for problem 3
plt.show()
