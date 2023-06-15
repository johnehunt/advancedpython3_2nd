import pymysql


class Student:
    def __init__(self, student_id, name, surname, subject, email, year):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.subject = subject
        self.email = email
        self.year = year

    def __str__(self):
        return f'Student[{self.student_id}] {self.name} {self.surname} - {self.subject} {self.email} {self.year}'


# Open database connection
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='password',
                             database='uni-database')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute SQL query using execute() method.
cursor.execute('SELECT * FROM students')

# Fetch all the rows
data = cursor.fetchall()

# Convert data into Student objects
for row in data:
    student_id, name, surname, subject, email, year = row
    student = Student(student_id, name, surname, subject, email, year)
    print(student)

# disconnect from server
connection.close()
