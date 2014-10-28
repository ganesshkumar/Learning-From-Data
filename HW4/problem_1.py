import math

Dvc = 10
delta = 0.05

def calculate_epsilon(N):
  return math.sqrt((8*math.log((4*math.pow(2*N,Dvc))/delta)/N))

def problem_1():
  # Least N for which epsilon should not exceed 0.05
  options = [400000, 420000, 440000, 460000, 480000]
  for N in options:
    print "N=",N," Epsilon=",calculate_epsilon(N)

if __name__ == "__main__":
  problem_1()
