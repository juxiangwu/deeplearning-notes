#coding:utf-8
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

def plot3d(X,Y,Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    Gx, Gy = np.gradient(Z) # gradients with respect to x and y
    G = (Gx**2+Gy**2)**.5  # gradient magnitude
    N = G/G.max()  # normalize 0..1
    surf = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1,facecolors=cm.jet(N),
    linewidth=0, antialiased=False, shade=False)
    plt.show()

x = np.array([-1, 0, 1])
y = np.array([-2, 0, 2])
X, Y = np.meshgrid(x, y)
Z = (X + Y) ** 2 * np.sin(X)

plot3d(X,Y,Z)




