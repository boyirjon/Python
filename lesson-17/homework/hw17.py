# Homework 1

# Task 1

import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})

# Task 2

print(df.head(3))

# Task 3

mean_age = df['age'].mean()
print(mean_age)

# Task 4

print(df[['first_name', 'City']])

# Task 5

import numpy as np
df['Salary'] = np.random.randint(50000, 100000, size=len(df))
print(df)

# Task 6

print(df.describe()

# Homework 2

# Task 1

import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

df = pd.DataFrame(data)

print(df)

# Task 2

max_sales = df['Sales'].max()
max_expenses = df['Expenses'].max()

print("Eng katta Sales:", max_sales)
print("Eng katta Expenses:", max_expenses)

# Task 3

min_sales = df['Sales'].min()
min_expenses = df['Expenses'].min()

print("Eng kichik Sales:", min_sales)
print("Eng kichik Expenses:", min_expenses)

# Task 4

avg_sales = df['Sales'].mean()
avg_expenses = df['Expenses'].mean()

print("O‘rtacha Sales:", avg_sales)
print("O‘rtacha Expenses:", avg_expenses)

# Homework 3

# Task 1

import pandas as pd

data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

df = pd.DataFrame(data)

print(df)

# Task 2

df['Max Expense'] = df[['January', 'February', 'March', 'April']].max(axis=1)

print(df[['Category', 'Max Expense']])

# Task 3

df['Min Expense'] = df[['January', 'February', 'March', 'April']].min(axis=1)

print(df[['Category', 'Min Expense']])

# Task 4

df['Average Expense'] = df[['January', 'February', 'March', 'April']].mean(axis=1)

print(df[['Category', 'Average Expense']])

expenses = df.set_index('Category')

print(expenses)
