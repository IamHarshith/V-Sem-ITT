num  = input("Enter the number of elements:\n")
arr = []
temp=0
for i in range(num):
    k= input("Enter the element:\n")
    arr.append(k)
for i  in range(num):
    for j in range(num):
        if(arr[i]<arr[j]):
            temp = arr[j]
            arr[j]=arr[i]
            arr[i]=temp
print "Sorted array: ",arr
    
