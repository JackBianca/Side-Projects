# Jack Bianca - 5/31/23
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Program to create a 3d plot or chart
# will further apply to Panel with bokeh plots

# Single points
ax = plt.axes(projection="3d")

x_data = np.arange(0,50,0.1)
y_data = np.arange(0,50,0.1)
z_data = np.sin(x_data) * np.cos(y_data)

ax.plot(x_data, y_data, z_data)
ax.set_title('Funny Function')
ax.set_xlabel('X Values (cm)')
ax.set_ylabel('Y Values (v)')
ax.set_zlabel('Fancy Results')
plt.show()
