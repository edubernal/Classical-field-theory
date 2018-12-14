import sys, time
import numpy as np
import scipy as scipy
from scipy.special  import *
import matplotlib.pyplot as plt
from matplotlib import cm
 
x = np.arange(0, 5, 0.1)

y0 = scipy.special.kv(0, x)
y1 = scipy.special.kv(1, x)
y2 = scipy.special.kv(2, x)
y3 = scipy.special.kv(3, x)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.plot(x,y0,'r-',x,y1,'b--',x,y2,'g-.',x,y3,'k:')
plt.xlim(0.23,4)
plt.ylim(0,4)
plt.xlabel ( r'$x$' )
plt.legend([r'$K_0$',r'$K_1$',r'$K_2$',r'$K_3$'])
plt.title ( r' $K_{\nu}(x) $' )
plt.show()