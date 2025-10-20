# DataFrame 1: Student Grades

# Task 1

import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)

print(df1)

# Task 2

top_student_index = df1['Average'].idxmax()

top_student = df1.loc[top_student_index]

print("Eng yuqori o‘rtacha bahoga ega talaba:")
print(top_student)

# Task 3

df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)

print(df1)

# Task 4

import matplotlib.pyplot as plt

subject_averages = df1[['Math', 'English', 'Science']].mean()

plt.bar(subject_averages.index, subject_averages.values)

plt.title('Average Grades by Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Grade')

plt.show()

# DataFrame 2: Sales Data

# Task 1

import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()

print("Total sales for each product:")
print(total_sales)

# Task 2

df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)

max_sales_index = df2['Total_Sales'].idxmax()

highest_sales_day = df2.loc[max_sales_index]

print("Eng yuqori jami sotuv bo‘lgan sana:")
print(highest_sales_day)

# Task 3

df2['Product_A_%Change'] = df2['Product_A'].pct_change() * 100
df2['Product_B_%Change'] = df2['Product_B'].pct_change() * 100
df2['Product_C_%Change'] = df2['Product_C'].pct_change() * 100

print(df2)

# Task 4

import matplotlib.pyplot as plt

plt.plot(df2['Date'], df2['Product_A'], label='Product A')
plt.plot(df2['Date'], df2['Product_B'], label='Product B')
plt.plot(df2['Date'], df2['Product_C'], label='Product C')

plt.title('Sales Trends for Each Product Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)

plt.show()

# DataFrame 3: Employee Information

# Task 1

import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

avg_salary = df3.groupby('Department')['Salary'].mean()

print("Average salary by department:")
print(avg_salary)

# Task 2

max_exp_index = df3['Experience (Years)'].idxmax()

most_experienced_employee = df3.loc[max_exp_index]

print("Eng ko‘p tajribaga ega xodim:")
print(most_experienced_employee)

# Task 3

min_salary = df3['Salary'].min()

df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary) * 100

print(df3)

# Task 4

import matplotlib.pyplot as plt

dept_counts = df3['Department'].value_counts()

plt.bar(dept_counts.index, dept_counts.values)

plt.title('Number of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')

plt.show()

# DataFrame 4: Customer Orders

# Task 1

import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

total_revenue = df4['Total_Price'].sum()

print("Umumiy daromad:", total_revenue)

# Task 2

most_ordered_product = df4['Product'].value_counts().idxmax()

most_ordered_count = df4['Product'].value_counts().max()

print(f"Eng ko‘p buyurtma qilingan mahsulot: {most_ordered_product} ({most_ordered_count} ta buyurtma)")

# Task 3

average_quantity = df4['Quantity'].mean()

print("O‘rtacha buyurtma miqdori:", average_quantity)

# Task 4

import matplotlib.pyplot as plt

sales_by_product = df4.groupby('Product')['Total_Price'].sum()

plt.pie(
    sales_by_product.values,            
    labels=sales_by_product.index,      
    autopct='%1.1f%%',                  
    startangle=90,                      
    shadow=True                         
)

plt.title('Sales Distribution by Product')

plt.show()
