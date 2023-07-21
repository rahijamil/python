from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 4])

random.shuffle(arr)
random.permutation(arr)

print(arr)