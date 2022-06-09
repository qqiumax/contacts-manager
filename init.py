import pymysql
import time
def init():
    connect = pymysql.connect(host='localhost',user='root',password='m@xQzc010810',charset='utf8mb4')
    cursor = connect.cursor()
    clear = 'drop DATABASE contacts;'
    cursor.execute(clear)
    createdb = "CREATE DATABASE IF NOT EXISTS contacts;"
    cursor.execute(createdb)
    cursor.close()
    connect.close()
    connect = pymysql.connect(host='localhost',database="contacts",user='root',password='m@xQzc010810',charset='utf8mb4')
    cursor = connect.cursor()
    print("created database")
    createtb = '''
    CREATE TABLE basic_info
    (
    name varchar(200) primary key,
    gender varchar(10),
    birthday varchar(9),
    number varchar(12),
    email varchar(100)
    );
    '''
    cursor.execute(createtb)
    print("created table")
    initl = '''
INSERT INTO basic_info (name,gender,birthday,number,email)
VALUES
("Max Qiu", "Male", "20100808", "17807501770","maxqqqq@hotmail.com")

'''
    cursor.execute(initl)
    show = 'SELECT * FROM basic_info;'
    result = cursor.execute(show)
    print(result)
    content = cursor.fetchall()
    print(content)
    connect.commit()
    cursor.close()
    connect.close()
    time.sleep(1)
init()
