from Line import Line
from Preceptron import Preceptron

def preceptron_learning():
  line = Line()
  line.random_line()
  sample = line.generate_sample(100)
  # print sample

  p = Preceptron([.01,0])
  p.learn(sample)

  sample = line.generate_sample(100000)

  incorrect = p.fng(sample)
  #print p.weight
  #print p.count

  return p.count, incorrect


if __name__ == "__main__":
  count = 0
  incorrect = 0

  for i in xrange (0,1000):
    print "Iteration ", i+1
    c,i = preceptron_learning()
    count += c
    incorrect += i

  print "Total iteration (1000 leearnings) :", count
  print "Averate iteration :", count/1000

  print "Incorrect points: ", incorrect
  print "Incorrect probability: ", float(incorrect)/(100000000)
