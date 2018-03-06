import re
str=raw_input("Enter the string:\n")
pla = raw_input("Enter the string to be replaced:\n")
rep = raw_input("Enter the string to replace:\n")
print re.sub(pla, rep, str)
#print output
