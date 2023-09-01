import mysql.connector

host = 'localhost'
user = 'root'
pass_ = 'qweasd'

db = mysql.connector.connect(
    host=host,
    user=user,
    passwd=pass_
)

# prepare cursor object
cursorObject = db.cursor()

# Create database
cursorObject.execute("CREATE DATABASE base")

print("Done!")