import math

sd = 0.1
d = 8

def expected_error(N):
  return (sd**2)*(1-float(d+1)/N)

if __name__ == "__main__":
  print "Expected error for N=10  is ",expected_error(10)
  print "Expected error for N=25  is ",expected_error(25)
  print "Expected error for N=100  is ",expected_error(100)
  print "Expected error for N=500  is ",expected_error(500)
  print "Expected error for N=1000  is ",expected_error(1000)
