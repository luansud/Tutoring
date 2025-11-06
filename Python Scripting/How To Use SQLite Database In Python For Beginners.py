import sqlite3
import pandas as pd 

#Drop the database if it exists
import os
if os.path.exists("student.db"):
    os.remove("student.db")

# Create a database
connection = sqlite3.connect('student.db')
cursor = connection.cursor()

# Create a Table
sql_create_table = '''
CREATE TABLE students (
    student_id TEXT PRIMARY KEY,
    student_name TEXT NOT NULL,
    gender TEXT,
    major TEXT,
    year_enrolled INTEGER,
    email TEXT UNIQUE
)
'''

cursor.connection.cursor()
try:
    cursor.execute(sql_create_table)
    connection.commit()
    print("Table created successfully.")
except Exception as e:
    print(f"Error creating table: {e}")
    print(e)
    connection.rollback()

# Insert Records
cursor.execute("INSERT INTO students VALUES ('A1', 'John Doe','M', 'Computer Science', 2020, 'adsasdasd@hotmail.com')")
cursor.execute("INSERT INTO students VALUES ('A2', 'Alton','M', 'Computer Science', 2020, 'afffffsdasd@hotmail.com')")
cursor.execute("INSERT INTO students VALUES ('A3', 'Stefanie','F', 'Computer Science', 2020,'bbbbbbbbasd@hotmail.com')")
cursor.execute("INSERT INTO students VALUES ('A4', 'Mike','M', 'Computer Science', 2020,'yyyyyyyasd@hotmail.com')")
connection.commit()
print("Records inserted successfully.")

# Query Records
sql_query = """SELECT * FROM students LIMIT 15"""

rows = cursor.execute(sql_query).fetchall()
columns = [col[0] for col in cursor.description]
df = pd.DataFrame(rows, columns=columns)
connection.close()
print(df)
print(columns)

# Using With statement to auto close connections
