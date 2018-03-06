string = raw_input("Enter the string:\n")
ch = int(input("1.Encryption.\n2.Decryption.:\n"))
shift = int(input("Enter the shift:\n"))
j=0
new=[]
new1=[]
l = len(string)
for i in range(l):
    new.append([0])
for i in range(l):
    new1.append([0])
if(ch==1):
    for i in range(l):
        j=int(ord(string[i]))
        #print(j)
        for k in range(1):
            j=j+shift
            if j>122:
                j=j-26
            if j>90:
                if j<97:
                    j=j-26
        new[i] = chr(j)
    for i in range(l):
        print new[i],
elif(ch==2):
    for i in range(l):
        j=int(ord(string[i]))
        #print(j)
        for k in range(1):
            j=j-shift
            if j<65:
                j=j+26
            if j<97:
                if j>90:
                    j=j+26
        new[i] = chr(j)
    for i in range(l):
        print new[i],
else:
    ("Invalid Choice")
    
