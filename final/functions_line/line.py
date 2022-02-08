# select a proper range of the variable x
# visualize the line y =  mx + b where b=30 and m = 0.5


import matplotlib.pyplot as plt
import numpy as np


x = np.array(range(100))
y = 0.5*x + 30
plt.plot(x,y)

plt.show()
