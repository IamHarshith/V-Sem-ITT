num = int(input("Enter the size of list:\n"))
array = []
orra = []
j=0
for i in range(num):
    k=raw_input("Enter the element:\n")
    array.append(k)
    orra.append(k)
print "Original List ",array

for i in array:
    j=j-1 
    orra[j]=i
print "Reversed List ",orra
    

