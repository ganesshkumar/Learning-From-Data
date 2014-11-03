import math
lr = 0.1

def f(u,v):
  e_v = math.pow(math.e,v)
  e_u = math.pow(math.e,-u)
  return (u*e_v - 2*v*e_u)**2

def delta_fu(u,v):
  e_v = math.pow(math.e,v)
  e_u = math.pow(math.e,-u)
  return 2*(e_v + 2*v*e_u)*(u*e_v - 2*v*e_u)

def delta_fv(u,v):
  e_v = math.pow(math.e,v)
  e_u = math.pow(math.e,-u)
  return 2*(u*e_v - 2*v*e_u)*(u*e_v - 2*e_u)

if __name__ == "__main__":
  u = 1
  v = 1
  iteration = 0
  error = f(u,v)
  while(error > 1e-14):
    iteration += 1
    du = delta_fu(u,v)
    dv = delta_fv(u,v)
    u -= lr * du
    v -= lr * dv
    error = f(u,v)
  print "Number of iterations=",iteration
  print "Final (u,v) = (",u,",",v,")"
