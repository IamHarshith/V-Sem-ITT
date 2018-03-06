num = int(input("Enter the size of list:\n"))
arr = []
for i in range(num):
    k =raw_input("Enter the element:\n")
    arr.append(k)
print(list(set(arr)))
