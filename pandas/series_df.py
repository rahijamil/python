import pandas as pd

mydataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

df = pd.DataFrame(mydataset)
print(df)

a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)


calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df.loc[0])