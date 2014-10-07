from Line import Line
from LinearRegression import LinearRegression

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

  return e_in, e_out

if __name__ == "__main__":
  e_in = 0
  e_out = 0
  for i in xrange(0,1000):
    print "Iteration ", i+1
    ei, eo = linear_regression()
    e_in += ei
    e_out += eo
  print "In-sample error (Ein) :", float(e_in)/(N*1000)
  print "Out-sample error (Eout) :", float(e_out)/(1000*1000)
