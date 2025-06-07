# install mysql on your computer
#pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Root@1234'
)

#prepare a cursor object
cursorobject = dataBase.cursor()

# create a datbase

cursorobject.execute("CREATE DATABASE crm")
print("all done!")
