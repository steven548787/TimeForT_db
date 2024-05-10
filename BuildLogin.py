import sqlite3

database = sqlite3.connect('LoginAccount.db')

e_mail = str(input("E-mail "))
password = str(input("password "))
year = str(input("Birth year "))
month = str(input("Birth month "))
date = str(input("Birth date "))
school = str(input("Your school name "))
Like = str(input("Your favorite subject "))
dislike = str(input("Your hatest subject "))
Hobby = str(input("Interest "))
teach_type = str(input("Prefer mentor or ... "))

cursor = database.cursor()

insert = "INSERT INTO Teacher \
        VALUES ("+e_mail+","+password+","+year+","+date+","+school+","+Like+","+dislike+","+Hobby+","+teach_type+","+password+")"
success = cursor.execute(insert)
print(success)