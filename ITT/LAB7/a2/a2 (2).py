import sqlite3
conn=sqlite3.connect('student.db')

# conn.execute("CREATE TABLE courses (cid VARCHAR PRIMARY KEY, cname VARCHAR);")
# conn.execute("CREATE TABLE data (cid VARCHAR, marks INT, FOREIGN KEY(cid) REFERENCES courses(cid))")

# conn.execute("INSERT INTO courses VALUES ('es', 'Embedded Systems')");
# conn.execute("INSERT INTO courses VALUES ('os', 'Operating Systems')");
# conn.execute("INSERT INTO courses VALUES ('itt', 'Internet Tools and Technology')");
# conn.execute("INSERT INTO courses VALUES ('daa', 'Design and Analysis of Algorithms')");
# conn.execute("INSERT INTO courses VALUES ('ir', 'Information Retrieval')");

# conn.execute("INSERT INTO data VALUES ('es', 95)");
# conn.execute("INSERT INTO data VALUES ('os', 92)");
# conn.execute("INSERT INTO data VALUES ('itt', 93)");
# conn.execute("INSERT INTO data VALUES ('daa', 89)");
# conn.execute("INSERT INTO data VALUES ('ir', 92)");

total=0
cursor=conn.execute("SELECT * FROM courses NATURAL JOIN data")
print "Courses:"
for i in cursor:
	print "Course id:",i[0],"   Course name:",i[1],"   Marks:",i[2]
	total+=int(i[2])
print "Total:",total,"/ 500"

if total>450:
	grade="A"
elif total>375:
	grade="B"
elif total>300:
	grade="C"
elif total>225:
	grade="D"
elif total>175:
	grade="E"
else:
	grade="F"

print "Grade:",grade


conn.commit()
conn.close()