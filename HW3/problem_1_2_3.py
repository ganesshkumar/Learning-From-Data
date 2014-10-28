import numpy as np

def find_n(p, M, epsilon):
  return "N >= ", -(np.log(p) - np.log(2) - np.log(M)) / (2*epsilon*epsilon)

def find_p(N, M, epsilon):
  return "P = ", 2 * M * np.exp(-2 * epsilon * epsilon * N)

print find_n(.03, 100, .05)
