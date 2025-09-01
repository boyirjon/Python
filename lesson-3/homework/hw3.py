# Task 1

fruits = ["apple", "banana", "cherry", "mango", "orange"]
print(fruits[2])

# Task 2

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2

print(combined)

# Task 3

numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]

new_list = [first, middle, last]

print(new_list)

# Task 4

movies = ["Inception", "Interstellar", "The Dark Knight", "Avatar", "Titanic"]

print(tuple(movies))

# Task 5

cities = ["London", "Berlin", "Paris", "New York", "Tokyo"]

if "Paris" in cities:
    print("Paris ro'yxatda bor")
else:
    print("Paris ro'yxatda yo'q")

# Task 6

numbers = [1, 2, 3, 4, 5]
duplicate = numbers * 2

print(duplicate)

# Task 7

numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

# Task 8

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(numbers[3:7])

# Task 9

colors = ["red", "blue", "green", "blue", "yellow", "blue"]

count_blue = colors.count("blue")

print(count_blue)

# Task 10

animals = ("tiger", "elephant", "lion", "zebra", "monkey")

index_lion = animals.index("lion")

print(index_lion)

# Task 11

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged = tuple1 + tuple2

print(merged)

# Task 12

fruits = ["apple", "banana", "cherry", "mango"]

numbers = (10, 20, 30, 40, 50)

print("List uzunligi:", len(fruits))
print("Tuple uzunligi:", len(numbers))

# Task 13

numbers = (10, 20, 30, 40, 50)

print(list(numbers))

# Task 14

numbers = (15, 8, 22, 3, 19, 30, 7)

maximum = max(numbers)
minimum = min(numbers)

print("Eng katta:", maximum)
print("Eng kichik:", minimum)

# Task 15

words = ("python", "java", "c++", "ruby", "swift")

print(words[::-1])
