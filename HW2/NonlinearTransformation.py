import random

# Generating data/sample
# Create a random line (with non-negative slope)

class NonlinearTransformation:
  def __init__(self):
    self.sample = []

  def __random_sign(self):
    return 1 if random.random() > .5 else -1

  def generate_sample_one(self, n):
    ''' Genearte n samples from the equation (x1*x1) + (x2*x2) - 0.6'''
    self.sample = []
    for i in xrange(0, n):
      x1 = self.__random_sign() * random.random()
      x2 = self.__random_sign() * random.random()
      y = ((x1*x1) + (x2*x2) - 0.6)
      self.sample.append((x1, x2, self.__sign(y)))
    return self

  def generate_sample_two(self, n):
    ''' Genearte n samples from the equation (x1*x1) + (x2*x2) - 0.6
        but with modified feature vector of (1;x1;x2;x1x2;x1*x1;x2*x2) '''
    self.sample = []
    for i in xrange(0, n):
      x1 = self.__random_sign() * random.random()
      x2 = self.__random_sign() * random.random()
      y = ((x1*x1) + (x2*x2) - 0.6)
      self.sample.append((x1, x2, x1*x2, x1*x1, x2*x2, self.__sign(y)))
    return self

  def add_noise(self):
    '''Flipping sign of output for 10% of sample'''
    for i in xrange(0, int(len(self.sample)*.1)):
      rand = random.randrange(0,len(self.sample))
      self.sample[rand] = (self.sample[rand][:-1] + (-self.sample[rand][-1],))
    return self

  def get_sample(self):
    return self.sample

  def __sign(self, n):
    return 1 if n > 0 else -1 if n < 0 else 0
