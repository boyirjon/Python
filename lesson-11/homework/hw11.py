# Task 1

import venv
import subprocess
import sys

venv.create("myenv", with_pip=True)

subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

# Task 2

# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# main.py

import math_operations
import string_utils

# Math operations
print("Add:", math_operations.add(5, 3))
print("Subtract:", math_operations.subtract(10, 4))
print("Multiply:", math_operations.multiply(6, 7))
print("Divide:", math_operations.divide(8, 2))

# String utils
print("Reverse:", string_utils.reverse_string("Hello"))
print("Vowel count:", string_utils.count_vowels("Hello World"))

# Task 3

geometry/
    __init__.py
    circle.py

# geometry/circle.py

import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius

# geometry/__init__.py

from .circle import calculate_area, calculate_circumference

file_operations/
    __init__.py
    file_reader.py
    file_writer.py

# file_operations/file_reader.py

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# file_operations/file_writer.py

def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# file_operations/__init__.py

from .file_reader import read_file
from .file_writer import write_file

# main.py

from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# Geometry package
r = 5
print("Circle area:", calculate_area(r))
print("Circle circumference:", calculate_circumference(r))

# File operations package
file_name = "example.txt"

# Faylga yozish
write_file(file_name, "Salom, bu test fayl!")

# Faylni o‘qish
content = read_file(file_name)
print("File content:", content)
