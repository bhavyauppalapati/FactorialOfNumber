# prompt for a non negative integer
n = int(input("Enter a nonnegative integer:"))
# validate the input
while n<0:
     # re prompt for the nonnegative integer
     n = int(input("Enter a nonnegative integer:"))
fact = 1
# multiply integer 1 to n using a for loop
for i in range(1,n+1):
     fact = fact * i
# print the factorial standard output
print(fact)
