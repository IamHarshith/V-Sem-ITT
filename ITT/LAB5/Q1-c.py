r = int(input("Enter the rows:\n"))
c = int(input("Enter the columns:\n"))
m = []
n = []
res = []
sum=0
print("Mtrix A=\n")        
for i in range(0,r):
    m.append([])
    for j in range(0,c):
        k=int(input("Enter the Element:\n"))
        m[i].append(k)
r1 = int(input("Enter the rows:\n"))
c1 = int(input("Enter the columns:\n"))
if c==r1:        
    print("Mtrix B=\n")
    for i in range(0,r1):
        n.append([])
        for j in range(0,c1):
                k=int(input("Enter the Element:\n"))
                n[i].append(k)
    for i in range(0,r):
        res.append([])
        for j in range(0,c1):
            res[i].append(0)    
    for i in range(len(m)):
       for j in range(len(n[0])):
           for k in range(len(n)):
                res[i][j] = res[i][j]+(m[i][k] * n[k][j])
    print("Entered matrix A is:\n")
    for i in range(0,r):
        for j in range(0,c):
            print m[i][j],        
        print("\n")
    print("\n\n")
    print("Entered matrix B is:\n")
    for i in range(0,r1):
        for j in range(0,c1):
            print n[i][j],        
        print("\n")
    print("\n\n") 
    print("Result of matrix multiplication is:\n")
    for i in range(0,r):
        for j in range(0,c1):
            print res[i][j],        
        print("\n")
else:
    print("Matrix multification not possible!")
