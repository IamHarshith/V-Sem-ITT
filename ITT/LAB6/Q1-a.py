print "\t\tTo check whether the string is Palindrome or not\n"
str = raw_input("Enter the string:\n")
if str[0:]==str[::-1]:
    print "Palindrome"
else:
    print "Not a Palindrome"
