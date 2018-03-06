#!D:\Python 2.7\python.exe
from datetime import datetime
print "Content-type:text/html\r\n\r\n"
print "<html><body>"
print "<center><h2>",datetime.now().strftime("%H:%M:%S"),"</h2></center></body></html>"
