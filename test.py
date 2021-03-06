print("My First Python Code on Git")

# Try running this code
from matplotlib import pyplot as plt
import numpy as np

# Generate 50 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 50)
fig, ax = plt.subplots()

# Map each onto a scatterplot we'll create with Matplotlib
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
ax.set(title="Some random data, created with JupyterLab!")
plt.show()
