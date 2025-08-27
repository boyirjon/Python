#Task 1

name = input("Ismingizni kiriting: ")
birth_year = int(input("Tug'ilgan yilingizni kiriting: "))

print(f"Salom {name}, sizning yoshingiz {2025 - birth_year} da.")

#Task 2

txt = 'LMaasleitbtui'

print(txt[1::2])
print(txt[::2])

#Task 3

txt = 'MsaatmiazD'

print(txt[::2])
print(txt[-1::-2])

#Task 4

txt = "I'am John. I am from London"

area = txt.split("from")[-1].strip()

print("Residence area:", area)

#Task 5

text = input("Matn kiriting: ")
print(text[::-1])

#Task 6

text = input("Matn kiriting: ")

vowels = "aeiouAEIOU"

count = 0
for char in text:
    if char in vowels:
        count += 1

print("Unli harflar soni:", count)

#Task 7

numbers = input("Sonlarni probel bilan kiriting: ")

numbers = [int(x) for x in numbers.split()]

maximum = max(numbers)

print("Eng katta son:", maximum)

#Task 8

word = input("So'z kiriting: ")

reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} -> Palindrome")
else:
    print(f"{word} -> Palindrome emas")

# Task 9

email = input("Email kiriting: ")

domain = email.split("@")[-1]

print("Email domain:", domain)

# Task 10

import random
import string

length = int(input("Parol uzunligini kiriting: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("Yaratilgan parol:", password)
