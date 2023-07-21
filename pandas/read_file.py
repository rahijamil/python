import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 9999
df = pd.read_csv("https://www.w3schools.com/python/pandas/data.csv")

# new_df = df.dropna()
df.fillna(130, inplace=True)

df.plot()

plt.show()