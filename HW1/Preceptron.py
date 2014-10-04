class Preceptron:
  def __init__(self, weight_vector):
    # dimension - dimension of the preceptron vector
    # first element is the threshold
    self.weight = weight_vector
    self.count = 0

  def __sign(self, n):
    return 1 if n > 0 else -1 if n < 0 else 0

  def learn(self, sample):
    self.count += 1
    self.__learn(sample)
    while self.misclassified:
      self.count += 1
      self.__learn(sample)

  def __learn(self, sample):
    self.misclassified = False
    for point in sample:
      # weight[0] is threshold
      # sample[0] is x
      # weight[1] is weight for x
      # sample[1] is y
      #print "Weight vector ", self.weight
      t = self.weight[0] + (point[0] * self.weight[1])
      if self.__sign(t) is not self.__sign(point[1]):
        self.misclassified = True
        self.weight[1] = self.weight[1] + (self.__sign(point[1]) * point[0])
        self.weight[0] = self.weight[0] + (self.__sign(point[1]) * .01)
        return

  def fng(self, sample):
    incorrect = 0
    for point in sample:
      t = self.weight[0] + (point[0] * self.weight[1])
      if self.__sign(t) is not self.__sign(point[1]):
        incorrect += 1
    return incorrect
