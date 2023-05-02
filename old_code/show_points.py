import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# read the file and extract the coordinates
with open('example_output_neulay.csv', 'r') as f:
    lines = f.readlines()
    coords = [list(map(float, line.strip().split(','))) for line in lines]

 # convert the coordinates into numpy arrays
x = np.array([coord[0] for coord in coords])
y = np.array([coord[1] for coord in coords])
z = np.array([coord[2] for coord in coords])

print(x)

# create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

# set the labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot')

# show the plot
plt.savefig("example.pdf", format="pdf", bbox_inches="tight")

