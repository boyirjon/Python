# Task 1

import json

with open("student.json", "r", encoding="utf-8") as f:
    data = json.load(f)

students = data["students"]

for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}")
    print(f"Subjects: {', '.join(student['subjects'])}")
    print("Address:")
    print(f"  Street: {student['address']['street']}")
    print(f"  City: {student['address']['city']}")
    print(f"  State: {student['address']['state']}")
    print(f"  Zipcode: {student['address']['zipcode']}")
    print("-" * 40)

# Task 2

import requests

API_KEY = "439d26fb6d17c2d06a2f435bb2f66130"
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid=439d26fb6d17c2d06a2f435bb2f66130&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description.capitalize()}")
else:
    print("Xatolik yuz berdi:", response.status_code)

# Task 3

import json

FILE_NAME = "books.json"

def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"books": []}

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_book(title, author, year):
    data = load_data()
    books = data["books"]
    new_id = max([book["id"] for book in books], default=0) + 1
    new_book = {"id": new_id, "title": title, "author": author, "year": year}
    books.append(new_book)
    save_data(data)
    print(f"Kitob qo‘shildi: {title}")

def update_book(book_id, title=None, author=None, year=None):
    data = load_data()
    books = data["books"]
    for book in books:
        if book["id"] == book_id:
            if title: book["title"] = title
            if author: book["author"] = author
            if year: book["year"] = year
            save_data(data)
            print(f"Kitob yangilandi: {book['title']}")
            return
    print("Kitob topilmadi!")

def delete_book(book_id):
    data = load_data()
    books = data["books"]
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_data(data)
            print(f"Kitob o‘chirildi: {book['title']}")
            return
    print("Kitob topilmadi!")

if __name__ == "__main__":
    add_book("C++ for Beginners", "Alice Brown", 2021)
    update_book(1, title="Python Advanced")
    delete_book(2)

# Task 4

import requests
import random

API_KEY = "YOUR_API_KEY"  
URL = "http://www.omdbapi.com/"


def get_movies_by_genre(genre):
    params = {
        "apikey": API_KEY,
        "s": genre,  
        "type": "movie"
    }
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if "Search" in data:
            return data["Search"]
    return []


def recommend_movie(genre):
    movies = get_movies_by_genre(genre)
    if not movies:
        print("Bu janr bo‘yicha film topilmadi.")
        return

    movie = random.choice(movies)  
    movie_id = movie["imdbID"]

    params = {"apikey": API_KEY, "i": movie_id}
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        details = response.json()
        print(f"\nTavsiya etilgan film:")
        print(f"Title: {details['Title']}")
        print(f"Year: {details['Year']}")
        print(f"Genre: {details['Genre']}")
        print(f"IMDB Rating: {details['imdbRating']}")
        print(f"Plot: {details['Plot']}")
    else:
        print("Film tafsilotlarini olishda xatolik!")


if __name__ == "__main__":
    user_genre = input("Qaysi janrdagi film kerak? (masalan: Action, Comedy, Drama): ")
    recommend_movie(user_genre)
