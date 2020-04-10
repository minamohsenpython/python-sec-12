#!C:\Python36\python.exe
import cgi
import pymysql as pm
import hashlib
import apputility as u
print("Content-Type:text/html\n")
fields = cgi.FieldStorage()
username = fields.getvalue("username")
pass1 = fields.getvalue("password1")
pass2 = fields.getvalue("password2")
if u.verify(pass1, pass2, username):
    print("passwords does not match")
else:
    digest = hashlib.sha1()
    digest.update(pass1.encode())
    password = digest.hexdigest()
    sql = "insert into user values(%s,%s)"
    try:
        connection = pm.connect(host="localhost", user="test", password="test", db="myapp")
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))
        connection.commit()
    except Exception as e:
        print("DB Error or username Exists")
    else:
        print(f"Register completed successfully")