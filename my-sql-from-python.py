import os
import pymysql

#Get username
username = os.getenv("C9_USER")
print(username)

#Connect to database using pymysql.connect
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run Query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close SQL connection - even on failure
    connection.close()