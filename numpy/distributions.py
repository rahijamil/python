from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


sns.displot(random.normal(size=100))
plt.show()