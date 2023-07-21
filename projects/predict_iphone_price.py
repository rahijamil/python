import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

data = pd.read_csv("iphone_price.csv")

model = LinearRegression()

model.fit(data[["version"]], data[["price"]])
print(model.predict([[14]]))
print(model.predict([[30]]))