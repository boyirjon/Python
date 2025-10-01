# Task 1

from datetime import datetime
from dateutil.relativedelta import relativedelta

birthdate_str = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")

birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

today = datetime.today()

difference = relativedelta(today, birthdate)

print(f"Sizning yoshingiz: {difference.years} yil, {difference.months} oy, {difference.days} kun")

# Task 2

from datetime import datetime

birthdate_str = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

today = datetime.today()

this_year_birthday = birthdate.replace(year=today.year)

if this_year_birthday < today:
    next_birthday = this_year_birthday.replace(year=today.year + 1)
else:
    next_birthday = this_year_birthday

days_left = (next_birthday - today).days

print(f"Sizning keyingi tug‘ilgan kuningizga {days_left} kun qoldi.")

# Task 3

from datetime import datetime, timedelta

current_str = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
current_datetime = datetime.strptime(current_str, "%Y-%m-%d %H:%M")

hours = int(input("Meeting davomiyligi (soat): "))
minutes = int(input("Meeting davomiyligi (daqiqa): "))

duration = timedelta(hours=hours, minutes=minutes)
end_time = current_datetime + duration

print(f"Meeting tugash vaqti: {end_time.strftime('%Y-%m-%d %H:%M')}")

# Task 4

from datetime import datetime
from zoneinfo import ZoneInfo

date_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
current_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

current_tz = input("Hozirgi vaqtzonani kiriting (masalan: Asia/Tashkent): ")
target_tz = input("Qaysi vaqtzonaga o‘tkazmoqchisiz? (masalan: America/New_York): ")

current_datetime = current_datetime.replace(tzinfo=ZoneInfo(current_tz))

converted_datetime = current_datetime.astimezone(ZoneInfo(target_tz))

print("O‘tkazilgan sana va vaqt:", converted_datetime.strftime("%Y-%m-%d %H:%M"))

# Task 5

import time
from datetime import datetime

future_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

print("\nCountdown boshlanmoqda...\n")

while True:
    now = datetime.now()
    remaining = future_time - now

    if remaining.total_seconds() <= 0:
        print("\rVaqt tugadi! 🚀")
        break

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"\rQolgan vaqt: {days} kun, {hours:02d}:{minutes:02d}:{seconds:02d}", end="")

    time.sleep(1)

# Task 6

import re

email = input("Email manzilni kiriting: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Email manzil to‘g‘ri (Valid email).")
else:
    print("Email manzil noto‘g‘ri (Invalid email).")

# Task 7

phone = input("Telefon raqamini kiriting (faqat raqamlar): ")

if phone.isdigit() and len(phone) == 10:
    formatted = f"({phone[0:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatlangan telefon raqami:", formatted)
else:
    print("Noto‘g‘ri raqam! 10 ta raqam kiritishingiz kerak.")

# Task 8

import re

password = input("Parolni kiriting: ")

length_error = len(password) < 8
uppercase_error = not re.search(r"[A-Z]", password)
lowercase_error = not re.search(r"[a-z]", password)
digit_error = not re.search(r"[0-9]", password)
special_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

errors = []
if length_error:
    errors.append("Kamida 8 ta belgidan iborat bo‘lishi kerak.")
if uppercase_error:
    errors.append("Kamida bitta katta harf bo‘lishi kerak.")
if lowercase_error:
    errors.append("Kamida bitta kichik harf bo‘lishi kerak.")
if digit_error:
    errors.append("Kamida bitta raqam bo‘lishi kerak.")
if special_error:
    errors.append("Kamida bitta maxsus belgi bo‘lishi kerak (!@#$...).")

if not errors:
    print("Parol kuchli!")
else:
    print("Parol zaif. Sabablari:")
    for e in errors:
        print("-", e)

# Task 9

text = """Python is a powerful programming language.
Python is easy to learn.
Many developers love Python because it is versatile."""

word = input("Qaysi so‘zni qidirmoqchisiz? ")

indices = []
start = 0

while True:
    index = text.lower().find(word.lower(), start)
    if index == -1:
        break
    indices.append(index)
    start = index + 1

if indices:
    print(f"'{word}' so‘zi matnda {len(indices)} marta uchradi.")
    print("Indekslari:", indices)
else:
    print(f"'{word}' so‘zi matnda topilmadi.")

# Task 10

import re

text = input("Matnni kiriting: ")

pattern = r'\b(?:\d{4}-\d{2}-\d{2}|\d{2}[/-]\d{2}[/-]\d{4})\b'

dates = re.findall(pattern, text)

if dates:
    print("Matndan topilgan sanalar:")
    for d in dates:
        print("-", d)
else:
    print("Matndan sana topilmadi.")
