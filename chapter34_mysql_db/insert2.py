import pymysql

# Open database connection
# Open database connection
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='password',
                             database='uni-database')
connection.autocommit(False)

# prepare a cursor object using cursor() method
cursor = connection.cursor()

try:
    # Execute INSERT command
    cursor.execute(
        "INSERT INTO students (id, name, surname, subject, email, year) VALUES (9, 'Denise', 'Byrne', 'History', 'db@my.com', 1)")
    # Commit the changes to the database
    connection.commit()
except:
    # Something went wrong
    # rollback the changes
    connection.rollback()

# Close the database connection
connection.close()
