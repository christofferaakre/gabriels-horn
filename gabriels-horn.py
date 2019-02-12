import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

u = 1
v = 1
a = 1

n = 10
step = 1 / 5
THETA = []
X = []
Y = []
Z = []

def x(u, v):
    return u

def y(u, v):
    return a * math.cos(v) / u

def z(u, v):
    return a * math.sin(v) / u

for i in range(0, int((n - 1) / step)):
    v = 1 + i * step
    for j in range(0, int((n - 1) / step)):
        u = 1 + j * step
        X.append(x(u, v))
        Y.append(y(u, v))
        Z.append(z(u, v))

fig = plt.figure()

plot = fig.add_subplot(111, projection='3d')

plot.scatter(X, Y, Z, s=35)

plt.show()