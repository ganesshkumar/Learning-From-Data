import math

B = {}

def b(N, k):
  if N is 1 and k is 1:
    return 1
  elif k is 1:
    return 1
  elif N is 1:
    return 2
  else:
    if (N,k) not in B:
      B[(N, k)] = b(N-1, k) + b(N-1, k-1)
    return B[(N, k)]

def is_break_point(N, f):
  ''' for the least value of N for which
      the growth function evaluates to anything less than 2**N
      then it is the break point of the growth function '''
  if f < 2**N:
    return True
  else:
    return False

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def function_1(N):
  ''' 1 + N '''
  return 1 + N

def function_2(N):
  ''' 1 + N + (N choose 2) '''
  return 1 + N + nCr(N,2)

def function_3(N):
  sum = 0
  for i in xrange(1, int(math.floor(math.sqrt(N))+1)):
    sum += nCr(N,i)
  return sum

def function_4(N):
  ''' 2 ** N/2 '''
  return 2 ** math.floor(N/2)

def function_5(N):
  ''' 2 ** N '''
  return 2 ** N


if __name__ == "__main__":
  break_point = None
  is_valid = True
  for i in xrange(1,10):
    # change the function here
    f = function_3(i)
    if break_point is None and is_break_point(i, f):
      break_point = i
    if break_point:
      bound = b(i, break_point)
      if f > bound:
        is_valid = False
        break
  print "Validity :", is_valid
