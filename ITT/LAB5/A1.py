m = int(input("Enter Lower limit:\n"))
n = int(input("Enter Upper limit:\n"))
prime = []
count=0
for i in range(m,n+1):
    if int(i/2)>=2:
        for j in range(2,int(i/2)+1):
            #print("i ",i," j ",j)
            if(i%j)==0:
                count=count+1
            else:
                1+2
        if(count<1):
            prime.append(i)
        count=0
    else:
        if i!=1:
            if i!=0:
                prime.append(i)
print "Prime numbers between ",m," and ",n ," are:\n"
print(prime)
