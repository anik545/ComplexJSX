from functools import partial

import time
import numpy
import scipy.optimize
import matplotlib.pyplot as pp
from sympy import arg,I
from math import atan2,sqrt,pi
from cmath import phase
from sympy import *


def z(x, y):
    n=x+y*1j
    return atan2(n.imag,n.real)-pi/4
    #return atan2(y-2,x-2)+pi/4

x_window = -10, 10
y_window = -10, 10

xs = []
ys = []
t1=time.time()
for x in numpy.linspace(*x_window, num=200):
    try:
        # A more efficient technique would use the last-found-y-value as a
        # starting point
        y = scipy.optimize.brentq(partial(z, x), *y_window)
    except ValueError:
        # Should we not be able to find a solution in this window.
        pass
    else:
        xs.append(x)
        ys.append(y)
t2=time.time()
print(t2-t1,'s')
pp.plot(xs, ys)
pp.xlim(*x_window)
pp.ylim(*y_window)
pp.show()
