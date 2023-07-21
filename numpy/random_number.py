from numpy import random

x = random.choice([3, 5, 7, 9], p=[.1, .3, .6, .0], size=(100))

print(x)
