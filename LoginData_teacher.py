import sqlite3

database = sqlite3.connect('LoginAccount.db')

e_mail = str(input("E-mail "))
password = str(input("password "))

cursor = database.cursor()

account = "select e_mail from Teacher where e_mail = '"+e_mail+"'"
secret = "select password from Teacher where e_mail = '"+e_mail+"' and password = '"+password+"'"

getmail = cursor.execute(account)
getPass = cursor.execute(secret)

if ( len(getmail.fetchall()) == 0 ):
    print("No account!! Please register!!")
    if ( len(getPass.fetchall()) == 0 ):
        print("Wrong Password! Please try again!")
else:
    print("Welcome!!")

cursor.close()