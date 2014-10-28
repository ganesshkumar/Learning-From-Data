import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
  return math.sin(math.pi*x)

m = []
variances = []
biases = []
x_set = []

for i in xrange(0,1000):
  if i % 100 is 0:
    print "iteration ",1+i
  x = list(np.random.uniform(-1,1,2))
  x_set.append(x)
  y = [f(i) for i in x]
  min_error = 99999999999999999999
  min_a = 0
  # This is too costly and inefficient
  # Replace with Linear Regression without the threshold
  for j in xrange(-1000, 1001):
    a = j*0.01
    errors = [(x[k]*a-y[k])**2 for k in xrange(0,len(x))]
    ms_error = np.average(errors)
    if ms_error < min_error:
      min_error = ms_error
      min_a = a
  m.append(min_a)

x = list(np.random.uniform(-1,1,2))
gbar_x = np.average(m)

for i in xrange(0,1000):
  if i % 100 is 0:
    print "iteration ",1+i
  x = x_set[i]
  min_a = m[0]
  variances.append(np.average([(min_a*x[z]-gbar_x*x[z])**2 for z in xrange(0,len(x))]))
  biases.extend([(x[i]*gbar_x-f(x[i]))**2 for i in xrange(len(x))])

variance = np.average(variances)
bias = np.average(biases)

print "gbar_x = ",gbar_x,"x"
print "bias = ", bias
print "variance = ", variance
