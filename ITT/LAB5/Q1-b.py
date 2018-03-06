r = input("Enter the rows:\n")
c = input("Enter the columns:\n")
m = []
t = []
for i in range(0,r):
    t.append([])
    for j in range(0,c):
        #k=int(input("Enter the Element:\n"))
        t[i].append(0)
for i in range(0,r):
    m.append([])
    for j in range(0,c):
        k=int(input("Enter the Element:\n"))
        m[i].append(k)
for i in range(0,r):
    for j in range(0,c):
        t[j][i]=m[i][j]
print("Entered matrix is:\n")
for i in range(0,r):
    for j in range(0,c):
        print m[i][j],
    print("\n")
print("Transpose of matrix is:\n")
for i in range(0,r):
    for j in range(0,c):
        print t[i][j],        
    print("\n")
