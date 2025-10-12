# Task 1

import numpy as np

my_list = [12.23, 13.32, 100, 36.32]
array = np.array(my_list)

print("Original List:", my_list)
print("One-dimensional NumPy array:", array)

# Task 2

import numpy as np

arr = np.arange(2, 11)
matrix = arr.reshape(3, 3)

print(matrix)

# Task 3

import numpy as np

vector = np.zeros(10)
print("Original Vector: ",vector)

vector[5] = 11
print(f"Updated Vector: {vector}")

# Task 4

import numpy as np

arr = np.arange(12, 38)
print(arr)

# Task 5

import numpy as np

arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(float)

print("Original array:", arr)
print("Converted to float:", float_arr)

# Task 6

import numpy as np

celsius = np.array([0, 12, 45.21, 34, 99.91, 0])

fahrenheit = celsius * 9/5 + 32

print("Values in Celsius degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

# Task 7

import numpy as np

arr = np.array([10, 20, 30])
new_values = [40, 50, 60, 70, 80, 90]

result = np.append(arr, new_values)

print("Original array:", arr)
print("After append values to the end of the array:", result)

# Task 8

import numpy as np

arr = np.random.randint(0, 100, 10)

mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)

print("Array:", arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)

# Task 9

import numpy as np

arr = np.random.rand(10, 10)

min_value = np.min(arr)

max_value = np.max(arr)

print("Array:\n", arr)
print("\nMinimum value:", min_value)
print("Maximum value:", max_value)

# Task 10

import numpy as np

arr = np.random.rand(3, 3, 3)

print(arr)
