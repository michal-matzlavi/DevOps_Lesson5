import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='XrgoYbWEBx', passwd='gZw75eRwWC', db='XrgoYbWEBx', autocommit=True)
cursor = conn.cursor()

""""
def create_dog(cursor, name, age, breed):
    cursor.execute(f"INSERT into dogs (name, age, breed) VALUES ('{name}', {age}, '{breed}')")


create_dog(cursor, "Simba", '5', "dog1")
create_dog(cursor, "Ravioli", '9', "dog2")
create_dog(cursor, "Rocki", '2', "dog3")
"""
#cursor.execute("UPDATE XrgoYbWEBx.dogs SET age = '10' WHERE name = 'Ravioli'")
cursor.execute("DELETE FROM XrgoYbWEBx.dogs WHERE name = 'w'")
cursor.execute("SELECT * FROM XrgoYbWEBx.dogs;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()