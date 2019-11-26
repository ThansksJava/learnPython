import mysql.connector
conn = mysql.connector.connect(user="root",password="",database="python")
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
conn.commit()
cursor.close()
