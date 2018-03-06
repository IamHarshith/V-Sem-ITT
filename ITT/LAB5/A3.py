num = int(input("Enter the size of list:\n"))
arr = []
sum=0
i=0
for i in range(num):
    k =input("Enter the element:\n")
    arr.append(k)
def sum(array):
    if len(array)==0:
        return 0
    else:
        return int(array[0]) + sum(array[1:]) 
print "Sum is ",sum(arr)

