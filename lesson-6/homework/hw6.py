# Modify String with Underscores

my_txt = "abcabcabcdeabcdefabcdefg"
used_chars = ['a', 'e', 'i', 'o', 'u']
i = 2
while i < len(my_txt) - 1:
    if my_txt[i] not in used_chars:
        my_txt = my_txt[:i + 1] + "_" + my_txt[i + 1:]
        used_chars.append(my_txt[i])
        i += 4
    else:
        i += 1
print(my_txt)

# Integer Squares Exercise

n = int(input("Son kiriting: "))

for i in range(n):
    print(i ** 2)

# Loop-Based Exercises

# Exercise 1

i = 1

while i <= 10:
    print(i)
    i += 1

# Exercise 2

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Exercise 3

n = int(input("Enter number: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum is:", total)

# Exercise 4

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n * i)

# Exercise 5

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    else:
        print(num)

# Exercise 6

n = int(input("Enter number: "))

count = 0
while n > 0:
    n //= 10
    count += 1

print("Total digits:", count)

# Exercise 7

n = 5

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8
# 1 - usul

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

# 2 - usul

list1 = [10, 20, 30, 40, 50]

i = len(list1) - 1
while i >= 0:
    print(list1[i])
    i -= 1


# Exercise 9
# 1 - usul

for i in range(-10, 0):
    print(i)

# 2 - usul

i = -10
while i < 0:
    print(i)
    i += 1

# Exercise 10

# for bilan

for i in range(5):
    print(i)

print("Done!")

# while bilan

i = 0
while i < 5:
    print(i)
    i += 1

print("Done!")

# Exercise 11

start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

# Exercise 12

n = 10

a, b = 0, 1
print("Fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Exercise 13

n = int(input("Enter number: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")

# Return Uncommon Elements of Lists

def uncommon_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for y in list2:
        if y not in list1:
            result.append(y)
    return result


print(uncommon_elements([1, 1, 2], [2, 3, 4]))
print(uncommon_elements([1, 2, 3], [4, 5, 6]))
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  
