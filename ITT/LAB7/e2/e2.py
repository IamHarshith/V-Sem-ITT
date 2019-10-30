import sqlite3
try:
	conn=sqlite3.connect('registration.db')
	conn.execute("CREATE TABLE data (phno VARCHAR PRIMARY KEY, name VARCHAR);")

regList=[]

cursor=conn.execute("SELECT * FROM data")

for i in cursor:
	regList.append(i[0])

name=raw_input("Enter name: ")
phno=raw_input("Enter contact number: ")

if phno in regList:
	print "Contact number already registered."
else:
	conn.execute("INSERT INTO data VALUES('"+phno+"', '"+name+"');")
	print "Successfully registered!"

conn.commit()
conn.close()
