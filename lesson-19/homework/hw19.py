# Homework Assignment 1: Analyzing Sales Data

# Task 1

import pandas as pd

url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-19/homework/task/sales_data.csv"
sales = pd.read_csv(url)

result = sales.groupby('Category').agg(
    Total_Quantity=('Quantity', 'sum'),
    Average_Price=('Price', 'mean'),
    Max_Quantity=('Quantity', 'max')
)

print(result)

# Task 2

import pandas as pd

url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-19/homework/task/sales_data.csv"
sales = pd.read_csv(url)

product_sales = sales.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

top_products = product_sales.loc[
    product_sales.groupby('Category')['Quantity'].idxmax()
]

print(top_products)

# Task 3

import pandas as pd

url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-19/homework/task/sales_data.csv"
sales = pd.read_csv(url)

sales['Total_Sales'] = sales['Quantity'] * sales['Price']

daily_sales = sales.groupby('Date')['Total_Sales'].sum().reset_index()

max_sales_date = daily_sales.loc[daily_sales['Total_Sales'].idxmax()]

print("Eng katta jami savdo bo‘lgan sana:")
print(max_sales_date)

# Homework Assignment 2: Examining Customer Orders

# Task 1

import pandas as pd

url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-19/homework/task/customer_orders.csv"
orders = pd.read_csv(url)

order_counts = orders.groupby('CustomerID')['OrderID'].count().reset_index(name='Total_Orders')

active_customers = order_counts[order_counts['Total_Orders'] >= 20]

print("20 yoki undan ko‘p buyurtma qilgan mijozlar:")
print(active_customers)

# Task 2

import pandas as pd

url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-19/homework/task/customer_orders.csv"
orders = pd.read_csv(url)

avg_price_per_customer = orders.groupby('CustomerID')['Price'].mean().reset_index(name='Average_Price')

high_value_customers = avg_price_per_customer[avg_price_per_customer['Average_Price'] > 120]

print("O‘rtacha narxi $120 dan yuqori bo‘lgan mijozlar:")
print(high_value_customers)

# Task 3

import pandas as pd

url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-19/homework/task/customer_orders.csv"
orders = pd.read_csv(url)

product_summary = orders.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Price', lambda x: (x * orders.loc[x.index, 'Quantity']).sum())
).reset_index()

filtered_products = product_summary[product_summary['Total_Quantity'] >= 5]

print("5 tadan kam sotilmagan mahsulotlar:")
print(filtered_products)

# Homework Assignment 3: Population Salary Analysis

import sqlite3
import pandas as pd

# 1️⃣ SQLite bazasidan population jadvalini o‘qish
conn = sqlite3.connect("task/population.db")
population = pd.read_sql_query("SELECT * FROM population;", conn)
conn.close()

# 2️⃣ Excel fayldan Salary Bandlarni o‘qish
salary_band = pd.read_excel("task/population salary analysis.xlsx")

# 3️⃣ Har bir odamni toifasini aniqlash uchun merge qilish
def categorize_salary(salary):
    for _, row in salary_band.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['Category']
    return 'Unknown'

population['SalaryCategory'] = population['Salary'].apply(categorize_salary)

# 4️⃣ Umumiy bo‘yicha hisob-kitob
summary = population.groupby('SalaryCategory').agg(
    PopulationCount=('Salary', 'count'),
    AverageSalary=('Salary', 'mean'),
    MedianSalary=('Salary', 'median')
).reset_index()

# 5️⃣ Foiz hisoblash
total_population = population.shape[0]
summary['PercentageOfPopulation'] = (summary['PopulationCount'] / total_population * 100).round(2)

# 6️⃣ Har bir State bo‘yicha hisob-kitob
state_summary = population.groupby(['State', 'SalaryCategory']).agg(
    PopulationCount=('Salary', 'count'),
    AverageSalary=('Salary', 'mean'),
    MedianSalary=('Salary', 'median')
).reset_index()

state_summary['PercentageOfPopulation'] = (
    state_summary.groupby('State')['PopulationCount']
    .transform(lambda x: x / x.sum() * 100)
).round(2)

# 7️⃣ Natijani Excelga yozish (xohlov bo‘yicha)
with pd.ExcelWriter("task/population_salary_report.xlsx") as writer:
    summary.to_excel(writer, sheet_name="Overall Summary", index=False)
    state_summary.to_excel(writer, sheet_name="By State", index=False)
