import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
  def __init__(self):
    self.x = []
    self.y = []
    pass

  def learn(self, sample):
    N = len(sample)
    d = len(sample[0]) # last element in the sample is output but will be replaced by x0

    for point in sample:
      self.x.append(1)
      self.x += list(point[:-1])
      self.y.append(point[-1])

    #self.x = np.array(self.x)
    #self.y = np.array(self.y)
    self.x = np.reshape(self.x, (N, d))
    self.y = np.reshape(self.y, (N, 1))

    xt = self.x.T # X-transpose
    xd = np.dot(np.linalg.inv(np.dot(xt, self.x)), xt) # X-dagger

    self.weight = np.dot(xd, self.y)

  def calculate_error(self, sample):
    error_count = 0
    for point in sample:
      x = np.array((1,) + point[:-1])
      y = np.dot(x, self.weight)
      if self.__sign(y) is not self.__sign(point[-1]):
        error_count += 1
    return error_count

  def plot(self, sample):
    N = len(sample)
    plt.plot([sample[i][0] for i in xrange(0,N)], [sample[i][1] for i in xrange(0,N)], 'ro')
    for point in sample:
      x = np.array([1, point[0]])
      y = np.dot(x, self.weight)
      plt.plot(x[1], self.__sign(y), 'ro')
    plt.axis([-1, 1, -1, 1])
    return plt

  def __sign(self, n):
    return 1 if n > 0 else -1 if n < 0 else 0
