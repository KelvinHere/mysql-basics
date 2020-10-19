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


### Simple Query, returns results as Tuples
#try:
#    # Run Query
#    with connection.cursor() as cursor:
#        sql = "SELECT * FROM Genre;"
#        cursor.execute(sql)
#        for row in cursor:
#            print(row)
#finally:
#    # Close SQL connection - even on failure
#    connection.close()

### Simple Query, returns results as Dict
#try:
#    # Run Query
#    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#        sql = "SELECT * FROM Genre;"
#        cursor.execute(sql)
#        for row in cursor:
#            print(row)
#finally:
#    # Close SQL connection - even on failure
#    connection.close()

### Create Table
#try:
#    # Run Query
#    with connection.cursor() as cursor:
#        cursor.execute("""CREATE TABLE IF NOT EXISTS
#            Friends(name char(20), age int, DOB datetime);""")
#        # Note that the above will still display a warning (not error) if the table already exists
#finally:
#    # Close SQL connection - even on failure
#    connection.close()

### Insert single row Data into table
#try:
#    with connection.cursor() as cursor:
#        row = ("Bob", 21, "1990-02-06 23:04:55") #Create variable for row Bob
#        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row) #Unpack each of the Tuples from row using %s
#        connection.commit()
#finally:
#    # Close SQL connection - even on failure
#    connection.close()        

### Insert Many
#try:
#    with connection.cursor() as cursor:
#        rows = [("Bob", 21, "1990-02-06 23:04:55"),
#                ("Jim", 56, "1970-02-06 21:08:33"),
#                ("Frank", 100, "1910-02-06 06:05:22"),
#                ("Harry", 11, "2000-02-06 23:04:55")] # List of Tuples
#        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows) #Execute many will cucle through the list of tuples
#        connection.commit() #SAVES CHANGES TO TABLE
#finally:
#    # Close SQL connection - even on failure
#    connection.close()

### Update a single row
#try:
#    with connection.cursor() as cursor:
#        cursor.execute("UPDATE Friends SET age = 22 Where name = 'Bob';")
#        connection.commit()
#finally:
#    # Close SQL connection - even on failure
#    connection.close()
#  

### Update a single row using string interpolation
#try:
#    with connection.cursor() as cursor:
#        cursor.execute("UPDATE Friends SET age = %s Where name = %s;",
#                        (23, 'Bob'))
#        connection.commit()
#finally:
#    # Close SQL connection - even on failure
#    connection.close()

### Update many
#try:
#    with connection.cursor() as cursor:
#        rows = [(23, 'Bob'),
#                (24, 'Jim'),
#                (25, 'Frank')]
#        cursor.executemany("UPDATE Friends SET age = %s Where name = %s;", rows)
#        connection.commit()
#finally:
#    # Close SQL connection - even on failure
#    connection.close()

### Delete Single Row
#try:
#    with connection.cursor() as cursor:
#        cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
#        connection.commit()
#finally:
#    # Close SQL connection - even on failure
#    connection.close()

### Delete - Alternate
#try:
#    with connection.cursor() as cursor:
#        cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Bob')
#        connection.commit()
#finally:
#    # Close SQL connection - even on failure
#    connection.close()

### Delete - Many
#try:
#    with connection.cursor() as cursor:
#        cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob', 'Jim'])
#        connection.commit()
#finally:
#    # Close SQL connection - even on failure
#    connection.close()

### Delete Where in (variable) - resulting command = "DELETE FROM Friends WHERE name in (%s,%s); ['Frank', 'Harry']"
#try:
#    with connection.cursor() as cursor:
#        list_of_names = ['Frank', 'Harry']
#        #Prepare a string with the same number of %s as in list_of_names
#        format_strings = ",".join(["%s"]*len(list_of_names))
#        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
#        connection.commit()
#finally:
    # Close SQL connection - even on failure
#    connection.close()