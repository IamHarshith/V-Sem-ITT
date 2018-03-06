#!C:\Python27\python.exe

import sqlite3

conn = sqlite3.connect('p.db')

conn.execute("create table if not exists student(regno PRIMARY KEY,name varchar,brach varchar,cgpa float);")

##conn.execute("insert into student values(150911032,'harshith','IT',8.0);")
##conn.execute("insert into student values(150911033,'rajath','CS',7.5);")
##conn.execute("insert into student values(150911034,'ramdev','EC',6.8);")
##conn.execute("insert into student values(150911035,'nagesh','EC',6.0);")
##conn.execute("insert into student values(150911036,'naveen','IT',9.4);")
##conn.execute("insert into student values(150911037,'harish','CS',7.8);")
#conn.execute("insert into student values(150911039,'arif','IT',8.9,20);")

cursor = conn.execute("select * from student where name like '%shi%' ")
print "TABLE CONTENT\n"
for i in cursor:
    print i[0],
    print i[1],
    print i[2],
    print i[3],
    print 


conn.commit()
conn.close()
