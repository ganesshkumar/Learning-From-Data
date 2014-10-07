from NonlinearTransformation import NonlinearTransformation
from LinearRegression import LinearRegression

# Size of training data
N = 1000

def linear_regression():
  transformation = NonlinearTransformation()
  sample = transformation.generate_sample_one(N).add_noise().get_sample()

  lr = LinearRegression()
  lr.learn(sample)

  # in-sample error
  e_in = lr.calculate_error(sample)

  # out-sample error
  #sample = transformation.generate_sample_one(100).add_noise().get_sample()
  e_out = 0#lr.calculate_error(sample)

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
  #print "Out-sample error (Eout) :", float(e_out)/(1000*1000)
