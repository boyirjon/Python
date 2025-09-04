# Task 1

def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2024))
print(is_leap(2023))

# Task 2

n = int(input().strip())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

# Task 3

a = int(input("a = "))
b = int(input("b = "))

if a % 2 != 0:
    a += 1

if b % 2 != 0:
    b -= 1

even_numbers = list(range(a, b + 1, 2))
print(even_numbers)

# Solution 2

a = int(input("a = "))
b = int(input("b = "))

even_numbers = list(range(a + a % 2, b - b % 2 + 1, 2))
print(even_numbers)
