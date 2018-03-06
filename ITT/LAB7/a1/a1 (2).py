import sqlite3
conn=sqlite3.connect('details.db')

# conn.execute("CREATE TABLE details (cid VARCHAR PRIMARY KEY, cname VARCHAR, phno VARCHAR, email VARCHAR);")

# conn.execute("INSERT INTO details VALUES('123', 'Vispi', '9870188858', 'vishtasp.sm@gmail.com')")
# conn.execute("INSERT INTO details VALUES('124', 'Hamsa', '17635', 'hamsa@gmail.com')")
# conn.execute("INSERT INTO details VALUES('125', 'AJ', '76534', 'aj@gmail.com')")
# conn.execute("INSERT INTO details VALUES('126', 'DT', '813265', 'd.t@gmail.com')")

ph=raw_input("Enter phone number: ")
em=raw_input("Enter email: ")

cursor=conn.execute("SELECT * FROM details")
found=0
for i in cursor:
	if i[2]==ph and i[3]==em:
		found=1
		print "Hello",i[1]
		break
if found==0:
	print "Please check credentials and try again"



conn.commit()
conn.close()