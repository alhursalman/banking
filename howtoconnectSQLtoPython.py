import os
from pymysql import connect

connection = connect(
      host =os.getenv("MYSQL_HOST"),             #"132.1.2.3"
      user =os.getenv("MYSQL_USER"),             #"root"
      password =os.getenv("MYSQL_PASSWORD"),     #"password"
      db=os.getenv("MYSQL_DATABASE"),            #"database"
      charset="utf8mb4"                       #"e44g4o6i0i3"
      )


with connection.cursor() as cursor:
      query = ('INSERT INTO account (Name, Balance) VALUES ("Bob", 1.0);')
      cursor.execute(query)
connection.commit()

with connection.cursor() as cursor:
    query = 'SELECT * FROM account;'
    cursor.execute(query)
    print(cursor.fetchall())

def AccountCreation():
    first_name = str(input("Enter your first name: ",))
    check = False
    while check == False:
        password = str(input("Enter your password: ",))
        password2 = str(input("Reenter your password: ",))
        if password == password2:
            check = True
    address = str(input("Enter your email address: ",))
    query = "INSERT INTO user (name,balance,password) VALUES(%s,%s,%s)"
    query2 = (name, balance, password)
    with connection.cursor() as cursor:
        cursor.execute(query,query2)
    connection.commit()
    print("Account has been created")
# 

connection.close()

"""try:
      with connection.cursor() as cursor:
            query ="insert into...;"
            cursor.execute(query)
      connection.commit()

      with connection.cursor() as cursor:
            query="SELECT * FROM book;"
            cursor.execute(query)
            result= cursor.fetchall()
            print (result)
finally:
      connection.close"""

#currentaccount = input("Welcome to your online banking. \n Do you currently have an account with us? y/n: )
#ca = currentaccount.lower()
#if ca is "y":
#      choice = input("Please enter credentials:")
#      ca_options = int(input("Select option: \n 1.Balance or Bank Statements \n 2.Withdrawal \n 3.Deposit \n 4. Exit \n")
