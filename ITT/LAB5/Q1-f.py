n=int(input("Enter number of term:\n"))
def recur(n):
   if n <= 1:
       return n
   else:
       return(recur(n-1) + recur(n-2))
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):    
           print recur(i),
