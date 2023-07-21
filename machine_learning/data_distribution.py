import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()