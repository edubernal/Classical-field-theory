import sys, time
import numpy as np
import scipy as scipy
from scipy.special  import *
import matplotlib.pyplot as plt
from matplotlib import cm
 
x = np.arange(0, 5, 0.25)

y0 = scipy.special.iv(0, x)
y1 = scipy.special.iv(1, x)
y2 = scipy.special.iv(2, x)
y3 = scipy.special.iv(3, x)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.plot(x,y0,'r-',x,y1,'b--',x,y2,'g-.',x,y3,'k:')
plt.xlim(0,4)
plt.ylim(0,4)
plt.xlabel ( r'$x$' )
plt.legend([r'$I_0$',r'$I_1$',r'$I_2$',r'$I_3$'])
plt.title ( r' $I_{\nu}(x) $' )
plt.show()

