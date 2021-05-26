import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def randrange(n, vmin, vmax):
    """
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(121 , projection = "3d")
n = 20

for c, m, zlow, zhigh in [( "g" , "+" , - 50 , - 25 )]:
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =c, marker =m, label = "20 punków")
ax.legend()


ax2 = fig.add_subplot(122 , projection = "3d")
t = np.linspace( 0 , 2 * np.pi, 5 )
z = t
x = np.sin(t)
y = np.cos(t)
ax2.plot(x, y, z, label = "5 punktów")
ax2.legend()
plt.show()