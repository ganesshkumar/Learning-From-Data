from Line import Line
from LinearRegression import LinearRegression
from Preceptron import Preceptron

# Size of training data
N = 100

def lr_booting_preceptron():
  line = Line()
  line.slanting_line()
  sample = line.generate_sample(N)

  lr = LinearRegression()
  lr.learn(sample)

  p = Preceptron(lr.weight)
  p.learn(sample)

  return p.count

if __name__ == "__main__":
  count = 0
  for i in xrange(0,1000):
    print "Iteration ", i+1
    count += lr_booting_preceptron()
  print "Average Count:", float(count)/1000
