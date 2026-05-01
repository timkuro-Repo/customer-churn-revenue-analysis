# Import pandas for loading, exploring, and analyzing tabular data
import pandas as pd

# Import matplotlib for creating charts and visualizations
import matplotlib.pyplot as plt


# Load the customer churn dataset from the CSV file into a pandas DataFrame
df = pd.read_csv("data/customer_churn.csv")


# Display the first 5 rows of the dataset
# This helps us quickly understand what the data looks like
print(df.head())

# Display basic information about the dataset
# This includes column names, data types, and missing values
print(df.info())

# Display summary statistics for numeric columns
# This includes count, mean, standard deviation, minimum, and maximum values
print(df.describe())


# Calculate the overall churn rate
# The "churned" column is assumed to use:
# 1 = customer churned
# 0 = customer did not churn
# Taking the mean gives the percentage of customers who churned
print("Churn Rate:")
print(df["churned"].mean() * 100)


# Calculate churn rate by subscription plan type
# groupby("plan_type") separates customers by plan
# mean() calculates the average churn value for each plan
# Multiplying by 100 converts the result into a percentage
print("Churn by Plan Type:")
print(df.groupby("plan_type")["churned"].mean() * 100)


# Calculate total revenue lost from customers who churned
# First, filter the dataset to only customers where churned == 1
# Then, sum their annual revenue
print("Revenue at Risk:")
print(df[df["churned"] == 1]["annual_revenue"].sum())


# Create a bar chart showing churn rate by plan type
# Each bar represents the average churn rate for one plan type
df.groupby("plan_type")["churned"].mean().plot(kind="bar")

# Add a clear chart title
plt.title("Churn Rate by Plan Type")

# Label the y-axis so viewers know the values represent churn rate
plt.ylabel("Churn Rate")

# Automatically adjust spacing so labels and titles are not cut off
plt.tight_layout()

# Save the chart as an image file in the images folder
plt.savefig("images/churn_by_plan.png")

# Display the chart on the screen
plt.show()