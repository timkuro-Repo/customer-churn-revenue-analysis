import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/customer_churn.csv")

print(df.head())
print(df.info())
print(df.describe(include="all"))

# Missing values
print(df.isnull().sum())

# Add your charts below.
# Example:
# df.select_dtypes(include="number").hist()
# plt.show()
