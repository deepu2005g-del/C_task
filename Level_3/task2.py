# Task 2: create a data visualization tool

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
file = input("Enter CSV file name: ")

if not os.path.exists(file):
    print("File not found. Please check path.")
    exit()

data = pd.read_csv(file)

print("\nColumns available:", data.columns)

x_col = input("Enter column for X-axis: ").strip().title()
y_col = input("Enter column for Y-axis: ").strip().title()

if x_col not in data.columns or y_col not in data.columns:
    print("Invalid column name. Choose from:", list(data.columns))
    exit()

plt.plot(data[x_col], data[y_col])
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title("Data Visualization")
plt.show()