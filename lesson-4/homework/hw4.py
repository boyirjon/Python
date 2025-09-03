# Dictionary Exercises

# Task 1

my_dict = {'a': 3, 'b': 1, 'c': 2}

ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Ascending:", ascending)

descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending:", descending)

# Task 2

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)

# Task 3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {**dic1, **dic2, **dic3}

print("Concatenated Dictionary:", new_dict)

# Task 4

n = 5
squares = {}

for x in range(1, n+1):
    squares[x] = x * x

print("Dictionary with squares:", squares)

# Task 5

squares = {}
for x in range(1, 16):
    squares[x] = x * x

print("Dictionary of squares:", squares)

# Set Exercises

# Task 1

my_set = set()

numbers = {1, 2, 3, 4, 5, 5}

print("Bo'sh set:", my_set)
print("Raqamlar seti:", numbers)

# Task 2

my_set = {"apple", "banana", "cherry"}

for item in my_set:
    print(item)

# Task 3
# Misol 1: Bitta element qo‘shish

my_set = {"apple", "banana"}
my_set.add("cherry")
print("Set:", my_set)

#Misol 2: Bir nechta element qo‘shish

my_set = {"apple", "banana"}
my_set.update(["cherry", "orange", "mango"])
print("Set:", my_set)

# Task 4

# 1-usul: .remove()

my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print("Set:", my_set)

# 2-usul: .discard()

my_set = {"apple", "banana", "cherry"}
my_set.discard("banana")
my_set.discard("orange")
print("Set:", my_set)

# 3-usul: .pop()

my_set = {"apple", "banana", "cherry"}

removed_item = my_set.pop()
print("Removed:", removed_item)
print("Set:", my_set)

# Task 5

my_set = {"apple", "banana", "cherry"}

item = "banana"

my_set.discard(item)

print("Set:", my_set)
