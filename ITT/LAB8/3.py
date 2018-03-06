#!D:\Python 2.7\python.exe
import cgi, random
username = cgi.FieldStorage().getvalue('username')
greetings = ["Hello,", "Welcome,", "Aloha,", "Bonjour,"]
index = random.randint(0,3)
print "Content-type:text/html\r\n\r\n"
print "<html><body>"
print "<p>",greetings[index],username,"!</p</body></html"
