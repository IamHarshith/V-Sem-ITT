#!D:\Python 2.7\python.exe
fo = open("foo.txt","r+")
visitor = int(fo.read(10))
fo.close()
fo = open("foo.txt","wb")
fo.write(str(visitor+1))
fo.close()

print "Content-type:text/html\r\n\r\n"
print "<html><body>"
print "<p>You are visitor",(visitor+1),"!</p></body></html>"
