# Task 1

side = float(input("Kvadratning tomonini kiriting: "))

perimeter = 4 * side
area = side ** 2

print("Kvadratning perimetri:", perimeter)
print("Kvadratning yuzi:", area)

# Task 2

import math

d = float(input("Aylananing diametrini kiriting: "))

length = math.pi * d

print("Aylananing uzunligi:", length)

# Task 3

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

mean = (a + b) / 2

print("Ikki sonning o'rtacha qiymati:", mean)

# Task 4

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2

print("Yig'indisi:", sum_ab)
print("Ko'paytmasi:", product_ab)
print("Birinchi sonning kvadrati:", square_a)
print("Ikkinchi sonning kvadrati:", square_b)
