import sqlite3
conn=sqlite3.connect('student.db')

# conn.execute("CREATE TABLE courses (cid VARCHAR PRIMARY KEY, cname VARCHAR);")
# conn.execute("CREATE TABLE student (sid VARCHAR PRIMARY KEY, sname VARCHAR);")
# conn.execute("CREATE TABLE data (cid VARCHAR, sid VARCHAR, marks INT, FOREIGN KEY(cid) REFERENCES " +
# 	"courses(cid), FOREIGN KEY(sid) REFERENCES student(sid));")

# conn.execute("INSERT INTO courses VALUES ('es', 'Embedded Systems')");
# conn.execute("INSERT INTO courses VALUES ('os', 'Operating Systems')");
# conn.execute("INSERT INTO courses VALUES ('itt', 'Internet Tools and Technology')");
# conn.execute("INSERT INTO courses VALUES ('daa', 'Design and Analysis of Algorithms')");
# conn.execute("INSERT INTO courses VALUES ('ir', 'Information Retrieval')");

# conn.execute("INSERT INTO student VALUES ('052', 'aaa')");
# conn.execute("INSERT INTO student VALUES ('058', 'bbb')");
# conn.execute("INSERT INTO student VALUES ('072', 'ccc')");
# conn.execute("INSERT INTO student VALUES ('142', 'ddd')");

# conn.execute("INSERT INTO data VALUES ('es', '052', 90)");
# conn.execute("INSERT INTO data VALUES ('es', '058', 95)");
# conn.execute("INSERT INTO data VALUES ('es', '072', 89)");
# conn.execute("INSERT INTO data VALUES ('es', '146', 91)");
# conn.execute("INSERT INTO data VALUES ('os', '052', 89)");
# conn.execute("INSERT INTO data VALUES ('os', '058', 92)");
# conn.execute("INSERT INTO data VALUES ('os', '072', 91)");
# conn.execute("INSERT INTO data VALUES ('os', '146', 90)");
# conn.execute("INSERT INTO data VALUES ('itt', '052', 95)");
# conn.execute("INSERT INTO data VALUES ('itt', '058', 97)");
# conn.execute("INSERT INTO data VALUES ('itt', '072', 95)");
# conn.execute("INSERT INTO data VALUES ('itt', '146', 90)");
# conn.execute("INSERT INTO data VALUES ('daa', '052', 86)");
# conn.execute("INSERT INTO data VALUES ('daa', '058', 89)");
# conn.execute("INSERT INTO data VALUES ('daa', '072', 87)");
# conn.execute("INSERT INTO data VALUES ('daa', '146', 82)");
# conn.execute("INSERT INTO data VALUES ('ir', '052', 92)");
# conn.execute("INSERT INTO data VALUES ('ir', '058', 96)");
# conn.execute("INSERT INTO data VALUES ('ir', '072', 92)");
# conn.execute("INSERT INTO data VALUES ('ir', '146', 90)");

cursor=conn.execute("SELECT * FROM courses")
print "Courses:"
for i in cursor:
	print "Course id:",i[0],"   Course name:",i[1]

cursor=conn.execute("SELECT * FROM student")
print "\nStudents:"
for i in cursor:
	print "Student id:",i[0],"   Student name:",i[1]

cid=raw_input("\nEnter course id: ")
sid=raw_input("Enter student id: ")

cursor=conn.execute("SELECT * FROM courses NATURAL JOIN data NATURAL JOIN student")
for i in cursor:
	if i[0]==cid and i[2]==sid:
		print "\n",i[1],"\n",i[4],"\nScore:",i[3]

conn.commit()
conn.close()