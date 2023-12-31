# Jack Bianca - 5/31/23
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')

x_data = np.arange(-5,5,0.1)
y_data = np.arange(-5,5,0.1)

X, Y = np.meshgrid(x_data, y_data)
Z = np.sin(X)*np.cos(Y)

ax.plot_surface(X,Y,Z,cmap='plasma')
plt.show()
