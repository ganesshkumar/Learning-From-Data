import random

# Generating data/sample
# Create a random line (with non-negative slope)

class Line:
  def __init__(self):
    self.slope = 0
    self.intercept = 0

  def random_line(self):
    ''' Create a random line '''
    s1 = 1 if random.random() > .5 else -1
    s2 = 1 if random.random() > .5 else -1
    positive_side = s1* random.random()  # corresponds to x = +1
    negative_side = s2 * random.random() # corresponds to x = -1

    self.slope = (positive_side - negative_side)/2
    self.intercept = positive_side - self.slope

  def generate_sample(self, n):
    ''' Genearte n samples from the line equation '''
    self.sample = []
    for i in xrange(0, n):
      sign = -1 if random.random() > 0.5 else 1
      x = sign * random.random()
      y = self.__solve(x)
      self.sample.append((x,self.__sign(y)))
    return self.sample

  def get_sample(self, n):
    return self.sample

  def __solve(self, x):
    ''' Solve the line equation for given x '''
    y = (self.slope * x) + self.intercept
    return y

  def __sign(self, n):
    return 1 if n > 0 else -1 if n < 0 else 0
