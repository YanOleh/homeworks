'''Хотел попрактиковаться именно через пайтон,
поэтому сделал в файле с расширением .py'''

import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#1 creat new table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

#2 rename table
cursor.execute('ALTER TABLE Users RENAME TO Users1')

#3 add new user
cursor.execute('INSERT INTO Users1 (username, email, age) VALUES (?, ?, ?)', ('newuser', 'g@g.com', 20))

#4 add new column
cursor.execute('ALTER TABLE Users1 ADD COLUMN city TEXT')

#5 update user
cursor.execute('UPDATE Users1 SET age = ? WHERE id = ?', (29, 1))

#6 delete user
cursor.execute('DELETE FROM Users1 WHERE id = ?', (1,))

connection.commit()
connection.close()
