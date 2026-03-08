import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

cursor.execute("INSERT INTO students (name, age, marks) VALUES ('Teja', 21, 85)")
cursor.execute("INSERT INTO students (name, age, marks) VALUES ('Ravi', 22, 75)")
cursor.execute("INSERT INTO students (name, age, marks) VALUES ('Anu', 20, 92)")

connection.commit()
connection.close()

print("Database created successfully!")
