num = int(input("Enter the number of item in the list:\n"))
lis = []
rev  = []
count=0;
c=0
for i in range(num):
    k = raw_input("Enter the value:\n")
    rev.append(k)
    lis.append(k)
lis.reverse()
#print(rev,lis)
for i in range(num):
    if(lis[i] == rev[i]):
        count=count+1
    else:
        print rev,
        print("not a palindrome")
        break
if(count==num):
    print lis,
    print(" is a Palindome")

string = raw_input("Enter the string:\n")
revs = string
for i in range(len(string)):
    if(string[i]==revs[(len(string)-1)-i]):
        c=c+1
if(c==len(string)):
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")
    
