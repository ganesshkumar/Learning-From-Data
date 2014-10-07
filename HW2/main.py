from Line import Line
from LinearRegression import LinearRegression
from Preceptron import Preceptron

# Size of training data
N = 100

def linear_regression():
  line = Line()
  line.slanting_line()
  sample = line.generate_sample(N)

  lr = LinearRegression()
  lr.learn(sample)

  # in-sample error
  e_in = lr.calculate_error(sample)
  # Plotting in-sample graph
  #plt = lr.plot(sample) #plot the samples
  #plt.plot([-lr.weight[0]/lr.weight[1] for y in xrange(-1,2)], [y for y in xrange(-1,2)]) # Add the x intercept line
  #plt.show()

  # out-sample error
  sample = line.generate_sample(1000)
  e_out = lr.calculate_error(sample)
  # Plotting out-sample graph
  #plt = lr.plot(sample) #plot the samples
  #plt.plot([-lr.weight[0]/lr.weight[1] for y in xrange(-1,2)], [y for y in xrange(-1,2)]) # Add the x intercept line
  #plt.show()

  #print "Line: slope=", line.slope, " intercept=", line.intercept
  #print "W_Vec: weight=", lr.weight[1], " threshold=", lr.weight[0]

  return e_in, e_out

def lr_booting_preceptron():
  line = Line()
  line.slanting_line()
  sample = line.generate_sample(N)

  lr = LinearRegression()
  lr.learn(sample)

  p = Preceptron(lr.weight)
  p.learn(sample)

  return p.count

def prob_linear_regression():
  e_in = 0
  e_out = 0
  for i in xrange(0,1000):
    print "Iteration ", i+1
    e_in, e_out = linear_regression()
  print "In-sample error (Ein) :", float(e_in)/(N*1000)
  print "Out-sample error (Eout) :", float(e_out)/(1000*1000)

def prob_lr_booting_preceptron():
  count = 0
  for i in xrange(0,1000):
    print "Iteration ", i+1
    count += lr_booting_preceptron()
  print "Average Count:", float(count)/1000


if __name__ == "__main__":
  prob_linear_regression()
