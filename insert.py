import pymysql
import time
connect = pymysql.connect(host='localhost',database="contacts",user='root',password='m@xQzc010810',charset='utf8mb4')
cursor = connect.cursor()
print("what aspects are there, pls input like (asp1,asp2....aspn)")
print("5 aspects are here are avalible: name, gender, birthday, number ,email")
aspx = input("here: ")
print("pls input content for aspects what you have just entered")
print("like ('content1', '2', '3')")
cont = input('here')
exe = "INSERT INTO basic_info" + aspx + "VALUES" + cont + ";"
cursor.execute(exe)
show = 'SELECT * FROM basic_info;'
result = cursor.execute(show)
print(result)
content = cursor.fetchall()
print(content)
connect.commit()
cursor.close()
connect.close()
time.sleep(1)
