import pymysql

# Open database connection
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='password',
                             database='uni-database')
connection.autocommit(False)

# prepare a cursor object using cursor() method
cursor = connection.cursor()

try:
    # Execute DELETE command
    cursor.execute("DELETE FROM students WHERE id = 9")

    # Commit the changes to the database
    connection.commit()
except:
    # rollback the changes if an exception / error
    connection.rollback()

# Close the database connection
connection.close()
