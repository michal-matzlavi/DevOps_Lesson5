import pymysql
connection = pymysql.connect(host = 'database-1.c65uwrrkzb8g.us-east-1.rds.amazonaws.com', port= 3306, user='michal', passwd='michal', db='michal', autocommit=True)


# opens a tab for query
cursor1 = connection.cursor()
# cursor1.execute("insert into animals values('spider', 8, 1)"
def create_animal(cursor):
    name = input("enter animal name: ")
    legs = input("enter legs: ")
    age = input("enter age: ")
    cursor.execute("insert into animals values('{name}', {legs}, {age})")
def animal_age(cursor, animal_name):
    cursor.execute("select ")
    cursor.execute("update animals set age ")

cursor1.execute("select * from animals")
for row in cursor1:
    print(row)

# cursor1.execute("insert into students values('3243423423', 'jkdflk', 'cnsdk', 78")
# cursor1.execute("delete from students where id = '3243423423')