print "\t\tTo print environmental variables\n"
import os
print "\n",os.environ,"\n\n"
str=raw_input("Enter the directory:\n")
print os.environ[str]

