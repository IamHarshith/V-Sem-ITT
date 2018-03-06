
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def pow(a,b):
    return a**b
print("1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.MOD\n6.POW")
a = int(input("Enter the first number:\n"))
c=str(a)
b = int(input("Enter the second number:\n"))
d=str(b)
ch = int(input("Enter the choice:\n"))
print("\n")
if(ch == 1):
    print c +" + "+d +" = " ,
    print add(a,b)
elif(ch==2):
    print c +" - "+d +" = " ,
    print sub(a,b)
elif(ch==3):
    print c +" * "+d +" = " ,
    print mul(a,b)
elif(ch==4):
    print c +" / "+d +" = " ,
    print div(a,b)
elif(ch==5):
    print c +" % "+d +" = " ,
    print mod(a,b)
elif(ch==6):
    print c +" ^ "+d +" = " ,
    print pow(a,b)   
else:
    print "Invalid Operation"
