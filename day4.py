#program to print sum of first n numbers
n=int(input("Enter number: "))
sum=0
while(n>0):
       sum=sum+n
       n=n-1
print("Sum of first n number is: ",sum)