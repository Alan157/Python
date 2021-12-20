import sqlite3

conn = sqlite3.connect('mysqlite.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS students
             (rollno real, name text, class real)''')

c.execute('''INSERT INTO students
             VALUES(1, 'Alex', 8)''')

# commit the changes to db
conn.commit()
print(c.fetchall())
# close the connection
conn.close()