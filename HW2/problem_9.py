import numpy as np

from NonlinearTransformation import NonlinearTransformation
from LinearRegression import LinearRegression

# Size of training data
N = 1000

def linear_regression():
  transformation = NonlinearTransformation()
  sample = transformation.generate_sample_two(N).add_noise().get_sample()

  lr = LinearRegression()
  lr.learn(sample)

  return lr.weight.flat

if __name__ == "__main__":
  vector = np.arange(float(6))
  iterations = 10000
  for i in xrange(0, iterations):
    vector += linear_regression()
  print [x/iterations for x in vector]
