n = input("Enter the number:\n")
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)



if n < 0:
   print("Enter a positive number")
else:
   print "The sum is",recur_sum(n)
