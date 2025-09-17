# Exception Handling Exercises

# Task 1

try:
    a = int(input("Birinchi sonni kirirting: "))
    b = int(input("Ikkinchi sonni kiriting: "))
    result = a / b
    print(f'Natija: {result}')
except ZeroDivisionError:
    print("Xatolik: Nolga bo‘lish mumkin emas!")
finally:
    print("Tugatildi")

# Task 2

try:
    number = int(input("Butun son kiriting: "))
    print(f"Siz kiritgan son: {number}")
except ValueError:
    print("Xatolik: Faqat butun son kiriting!")

# Task 3

filename = input("Fayl nomini kiriting: ")

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except FileNotFoundError:
    print(f"Xatolik: '{filename}' nomli fayl topilmadi!")

# Task 4

try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting:"))
    print(f"Yig'indi: {a + b}")
except ValueError:
    raise TypeError("Xatolik: Faqat son kiriting!")

# Task 5

try:
    with open("data.txt", "r") as file:
        file.write("Hello world!")
except PermissionError:
    print(f"Xatolik: 'data.txt' fayliga yozish uchun ruxsat yo‘q!")

# Task 6

try:
    numbers = [10, 20, 30, 40, 50]
    index = int(input("Qaysi indeksni chiqarishni xohlaysiz (0-4): "))
    print(f"Tanlangan element: {numbers[index]}")
except IndexError:
    print("Xatolik: Indeks ro‘yxat chegarasidan tashqarida!")
except ValueError:
    print("Xatolik: Faqat son kiriting!")

# Task 7

try:
    number = int(input("Son kiriting: "))
    print(f"Siz kiritgan son: {number}")
except KeyboardInterrupt:
    print("\nXatolik: Siz kiritishni bekor qildingiz (Ctrl + C bosdingiz).")

# Task 8

try:
    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))
    result = a / b
    print(f"Natija: {result}")
except ArithmeticError:
    print("Xatolik: Arifmetik xato yuz berdi (masalan, nolga bo‘lish).")
except ValueError:
    print("Xatolik: Faqat son kiriting!")

# Task 9

try:
    with open("data.txt", "r", encoding="ascii") as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("Xatolik: Faylni o‘qishda kodlash (encoding) muammosi yuz berdi!")
except FileNotFoundError:
    print("Xatolik: 'data.txt' fayli topilmadi.")

# Task 10

try:
    my_list = [1, 2, 3, 4, 5]

    my_list.push(10)
except AttributeError:
    print("Xatolik: List obyektida bunday metod yoki atribut mavjud emas!")

#File Input/Output Exercises

# Task 1

with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Task 2

def read_first_n_lines(filename, n):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' fayli topilmadi.")

n = int(input("Nechta qatorni o‘qishni xohlaysiz? "))
read_first_n_lines("data.txt", n)

# Task 3

with open("data.txt", "a", encoding="utf-8") as file:
    file.write("\nYangi qo‘shilgan matn.")

with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Fayl mazmuni:\n")
    print(content)

# Task 4

def read_last_n_lines(filename, n):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            last_lines = lines[-n:]
            for line in last_lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' fayli topilmadi.")

n = int(input("Oxiridan nechta qatorni o‘qishni xohlaysiz? "))
read_last_n_lines("data.txt", n)

# Task 5

def file_to_list(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' fayli topilmadi.")
        return []

lines_list = file_to_list("data.txt")
print("Fayldan o‘qilgan list:")
print(lines_list)

# Task 6

def file_to_variable(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = ""
            for line in file:
                lines += line
            return lines
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' fayli topilmadi.")
        return ""

text_variable = file_to_variable("data.txt")
print("Fayldagi matn:")
print(text_variable)

# Task 7

def file_to_array(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            array = []
            for line in file:
                array.append(line.strip())
            return array
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' fayli topilmadi.")
        return []

lines_array = file_to_array("data.txt")
print("Fayldan o‘qilgan array:")
print(lines_array)

# Task 8

def find_longest_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = file.read().split()
            max_length = len(max(words, key=len))
            longest_words = [word for word in words if len(word) == max_length]
            return longest_words
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' fayli topilmadi.")
        return []

longest = find_longest_words("data.txt")
print("Fayldagi eng uzun so‘zlar:")
print(longest)

# Task 9

def count_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            line_count = sum(1 for _ in file)
            return line_count
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' fayli topilmadi.")
        return 0

lines = count_lines("data.txt")
print(f"Faylda {lines} ta qator bor.")

# Task 10

def word_frequency(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()
            words = text.split()

            freq = {}
            for word in words:
                word = word.strip(".,!?;:\"'()[]{}")
                if word:
                    freq[word] = freq.get(word, 0) + 1
            return freq
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' fayli topilmadi.")
        return {}

frequencies = word_frequency("data.txt")
print("So‘zlarning chastotasi:")
for word, count in frequencies.items():
    print(f"{word}: {count}")

# Task 11

import os

def get_file_size(filename):
    try:
        size = os.path.getsize(filename)
        return size
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' fayli topilmadi.")
        return None

filename = "data.txt"
size = get_file_size(filename)
if size is not None:
    print(f"'{filename}' faylining hajmi: {size} bayt")

# Task 12

def write_list_to_file(filename, my_list):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for item in my_list:
                file.write(str(item) + "\n")
        print(f"List '{filename}' fayliga yozildi.")
    except Exception as e:
        print(f"Xatolik: {e}")

data = ["Salom", "Python", "Faylga yozish", 123, 45.6]
write_list_to_file("data.txt", data)

# Task 13

# copy_file.py

try:
    with open("source.txt", "r") as source:
        content = source.read()

    with open("destination.txt", "w") as destination:
        destination.write(content)

    print("Fayl muvaffaqiyatli nusxalandi!")

except FileNotFoundError:
    print("Xato: source.txt fayli topilmadi.")
except Exception as e:
    print(f"Noma’lum xato: {e}")

# Task 14

# combine_lines.py

try:
    with open("file1.txt", "r") as f1:
        lines1 = f1.readlines()

    with open("file2.txt", "r") as f2:
        lines2 = f2.readlines()

    with open("combined.txt", "w") as output:
        for line1, line2 in zip(lines1, lines2):
            combined = line1.strip() + " " + line2
            output.write(combined)

    print("Fayllar muvaffaqiyatli birlashtirildi! (natija combined.txt faylida)")

except FileNotFoundError as e:
    print(f"Fayl topilmadi: {e.filename}")
except Exception as e:
    print(f"Noma’lum xato: {e}")

# Task 15

import random

try:
    with open("data.txt", "r") as file:
        lines = file.readlines()

    if lines:
        random_line = random.choice(lines).strip()
        print(f"Tasodifiy qator: {random_line}")
    else:
        print("Fayl bo‘sh!")

except FileNotFoundError:
    print("Xatolik: 'data.txt' fayli topilmadi!")
except Exception as e:
    print(f"Noma’lum xatolik: {e}")

# Task 16

try:
    file = open("data.txt", "r")
    print(f"Fayl yopilganmi? {file.closed}")

    file.close()
    print(f"Fayl yopilganmi? {file.closed}")

except FileNotFoundError:
    print("Xatolik: 'data.txt' fayli topilmadi!")

# Task 17

try:
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]

    print("Newline belgilarisiz matn:")
    for line in lines:
        print(line)

except FileNotFoundError:
    print("Xatolik: 'data.txt' fayli topilmadi!")

# Task 18

import re

try:
    with open("data.txt", "r", encoding="utf-8") as file:
        text = file.read()

    words = re.findall(r"\w+", text)

    print(f"Fayldagi so‘zlar soni: {len(words)}")

except FileNotFoundError:
    print("Xatolik: 'data.txt' fayli topilmadi!")

# Task 19

import os

files = ["data1.txt", "data2.txt", "data3.txt"]

characters = []

for fname in files:
    try:
        with open(fname, "r", encoding="utf-8") as file:
            content = file.read()
            characters.extend(list(content))
    except FileNotFoundError:
        print(f"Xatolik: '{fname}' fayli topilmadi!")

print("Barcha belgilar listi:")
print(characters)

# Task 20

import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Bu {letter}.txt fayli\n")

print("A.txt dan Z.txt gacha bo‘lgan fayllar yaratildi!")

# Task 21

import string

def write_alphabet(filename, per_line=5):
    letters = string.ascii_uppercase
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(0, len(letters), per_line):
            file.write(letters[i:i+per_line] + "\n")

write_alphabet("alphabet.txt", per_line=5)

print("'alphabet.txt' fayli yaratildi!")
