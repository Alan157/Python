import sqlite3
from Students import Student


def create_student(f_name, l_name, age, grade):  # creates a student using the "Student" class
    s = Student()
    s.update_firstName(f_name)
    s.update_lastName(l_name)
    s.update_grade(age)
    s.set_age(grade)
    return s


def add_student(s):  # adds a student to the "students" table
    con_db.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                   (s.get_firstName(), s.get_lastName(), s.get_age(), s.get_grade()))


con_db = sqlite3.connect("students_db.db")  # creating the database

cur = con_db.cursor()  # assigning a cursor

cur.execute("""CREATE TABLE students (
    'First Name' text,
    'Last Name' text,
    Age integer,
    Grade integer);""")

#  creating students
s1 = create_student("Alan", "Tsypin", 25, 89)
s2 = create_student("Yuval", "Hershkovits", 25, 100)
s3 = create_student("Felix", "Lynal", 77, 77)

s_arr = [s1, s2, s3]  # used for adding in mass

for i in s_arr:  # adding students to the table
    add_student(i)

cur.execute("SELECT * FROM students")  # selecting all of the students for printing

print(cur.fetchall())  # printing all of the students in the table

con_db.commit()

con_db.close()
