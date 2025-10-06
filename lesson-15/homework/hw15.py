# Task 1

import sqlite3

connection = sqlite3.connect("animals.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

connection.commit()

connection.close()

print("Database va Roster jadvali muvaffaqiyatli yaratildi!")

# Task 2

import sqlite3

connection = sqlite3.connect("animals.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO Roster (Name, Species, Age) VALUES ('Benjamin Sisko', 'Human', 40)")
cursor.execute("INSERT INTO Roster (Name, Species, Age) VALUES ('Jadzia Dax', 'Trill', 300)")
cursor.execute("INSERT INTO Roster (Name, Species, Age) VALUES ('Kira Nerys', 'Bajoran', 29)")

connection.commit()

connection.close()

print("Roster jadvaliga ma'lumotlar muvaffaqiyatli qo'shildi!")

# Task 3

import sqlite3

connection = sqlite3.connect("animals.db")

cursor = connection.cursor()

cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

connection.commit()

connection.close()

print("Jadzia Dax nomi Ezri Dax ga yangilandi!")

# Task 4

import sqlite3

connection = sqlite3.connect("animals.db")

cursor = connection.cursor()

cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")

results = cursor.fetchall()

for row in results:
    print(row)

connection.close()
