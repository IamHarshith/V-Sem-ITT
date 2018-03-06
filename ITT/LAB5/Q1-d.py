r = int(input("Enter the rows:\n"))
c = int(input("Enter the columns:\n"))
m = []
n = []
s = []
for i in range(0,r):
    s.append([])
    for j in range(0,c):
        s[i].append(0)
for i in range(0,r):
    m.append([])
    for j in range(0,c):
        k=int(input("Enter the Element:\n"))
        m[i].append(k)
print("Enter the element of second matrix:\n")
for i in range(0,r):
    n.append([])
    for j in range(0,c):
        k=int(input("Enter the Element:\n"))
        n[i].append(k)
print("First Matrix is:\n")
for i in range(0,r):
    for j in range(0,c):
        print m[i][j],
    print("\n")
print("Second Matrix is:\n")
for i in range(0,r):
    for j in range(0,c):
        print n[i][j],
    print("\n")        
        
print("\n\n")    
print("Sum of matrix is:\n")
for i in range(0,r):
    for j in range(0,c):
        print m[i][j]+n[i][j],        
    print("\n")
