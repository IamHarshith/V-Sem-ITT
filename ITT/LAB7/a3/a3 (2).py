import sqlite3
conn=sqlite3.connect('bank.db')

# conn.execute("CREATE TABLE details (accno VARCHAR PRIMARY KEY, name VARCHAR, bal INT);")

# conn.execute("INSERT INTO details VALUES ('1234', 'Vispi', 100000)");
# conn.execute("INSERT INTO details VALUES ('1235', 'Hamsa', 50001)");
# conn.execute("INSERT INTO details VALUES ('1236', 'AJ', 10000)");
# conn.execute("INSERT INTO details VALUES ('1237', 'DT', 50000)");

acc=raw_input("Enter account number: ")
cursor=conn.execute("SELECT * FROM details WHERE accno='"+acc+"'")
for i in cursor:
	print "Account No:",i[0],"   Name:",i[1],"   Balance:",i[2]

print "\nAccounts with balance over 50000:"
cursor=conn.execute("SELECT * FROM details WHERE bal>50000")
for i in cursor:
	print "Account No:",i[0],"   Name:",i[1],"   Balance:",i[2]
conn.commit()
conn.close()