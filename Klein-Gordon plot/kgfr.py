import sys, time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
w = 1
p = w
x = np.arange(-3, 3, 0.25)
t = np.arange(0, 10, 0.25)

X, T = np.meshgrid(x, t)
u1 = np.cos(w*T-p*X)
u2 = np.sin(w*T-p*X)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))

#===============
#  First subplot
#===============
# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')


surf = ax.plot_surface(X, T, u1, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
plt.xlabel ( r'$x$' )
plt.ylabel ( r'$t$' )
plt.title ( r'  $\Re(\phi(x,t))$' )
#===============
# Second subplot
#===============
# set up the axes for the second plot
ax = fig.add_subplot(1, 2, 2, projection='3d')

surf = ax.plot_surface(X, T, u2, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.set_zlim(-1.01, 1.01)
plt.xlabel ( r'$x$' )
plt.ylabel ( r'$t$' )
plt.title ( r'  $\Im(\phi(x,t))$' )

plt.show()