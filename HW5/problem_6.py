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
  iteration = 1
  error = f(u,v)
  while (iteration <= 15):
    du = delta_fu(u,v)
    u -= lr * du
    dv = delta_fv(u,v)
    v -= lr * dv
    iteration += 1
  print "Final (u,v) = (",u,",",v,")"
  print "Final error = ", f(u,v)
