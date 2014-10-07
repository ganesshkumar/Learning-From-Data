import random

# Generating data/sample
# Create a random line (with non-negative slope)

class Line:
  def __init__(self):
    self.slope = 0
    self.intercept = 0

  def __random_sign(self):
    return 1 if random.random() > .5 else -1

  def random_line(self):
    ''' Create a random line '''
    x1 = self.__random_sign() * random.random()
    y1 = self.__random_sign() * random.random()
    x2 = self.__random_sign() * random.random()
    y2 = self.__random_sign() * random.random()

    self.slope = float(y2 - y1)/float(x2 - x1)
    self.intercept = y1 - (self.slope * x1)

  def slanting_line(self):
    ''' Create a slanting line '''
    sign = self.__random_sign()
    x1 = sign * random.random()
    x2 = -sign * random.random()
    sign = self.__random_sign()
    y1 = sign * random.random()
    y2 = -sign * random.random()

    self.slope = float(y2 - y1)/float(x2 - x1)
    self.intercept = y1 - (self.slope * x1)

  def generate_sample(self, n):
    ''' Genearte n samples from the line equation '''
    self.sample = []
    for i in xrange(0, n):
      sign = -1 if random.random() > 0.5 else 1
      x = sign * random.random()
      y = self.__solve(x)
      self.sample.append((x, self.__sign(y)))
    return self.sample

  def get_sample(self, n):
    return self.sample

  def __solve(self, x):
    ''' Solve the line equation for given x '''
    y = (self.slope * x) + self.intercept
    return y

  def __sign(self, n):
    return 1 if n > 0 else -1 if n < 0 else 0
