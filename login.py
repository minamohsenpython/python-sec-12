#!C:\Python36\python.exe
import cgi
import pymysql as pm
import hashlib

print("Content-Type:text/html\n")
fields = cgi.FieldStorage()
username = fields.getvalue("username")
pass1 = fields.getvalue("password")

digest = hashlib.sha1()
digest.update(pass1.encode())
password = digest.hexdigest()

sql = "select * from user where username=%s and password=%s"
try:
    connection = pm.connect(host="localhost", user="test", password="test", db="myapp")
    cursor = connection.cursor()
    cursor.execute(sql, (username, password))
    result = cursor.fetchall()
except Exception as e:
    print("DB Error")
else:
    if len(result) != 0:
        print("Welcome to your panel")
    else:
        print("username or password is not correct")