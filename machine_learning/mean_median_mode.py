from scipy import stats
import numpy as np

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

mean = np.mean(speed)
median = np.median(speed)
mode = stats.mode(speed)

print(mean)
print(median)
print(mode)