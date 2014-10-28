import math
import matplotlib.pyplot as plt

N = 6

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

plt.plot([i for i in xrange(3,N)], [2**i for i in xrange(3,N)])
#plt.plot([i for i in xrange(3,N)], [nCr(i+1, 4) for i in xrange(3,N)])
#plt.plot([i for i in xrange(3,N)], [nCr(i+1, 2)+1 for i in xrange(3,N)])
plt.plot([i for i in xrange(3,N)], [nCr(i+1, 4)+nCr(i+1, 2)+1 for i in xrange(3,N)])
#plt.plot([i for i in xrange(3,N)], [nCr(i+1, 4)+nCr(i+1, 3)+nCr(i+1, 2)+nCr(i+1, 1)+1 for i in xrange(3,N)])
plt.show()
