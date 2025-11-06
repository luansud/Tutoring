import sqlite3
import pandas as pd

connection = sqlite3.connect('musics.db')
cursor = connection.cursor()

rows = cursor.execute("""SELECT * FROM customers LIMIT 15""").fetchall()
columns = [col[0] for col in cursor.description]
df = pd.DataFrame(rows, columns=columns)
connection.close()

print(df)
print(columns)
print(df.to_csv('musics.csv'))
