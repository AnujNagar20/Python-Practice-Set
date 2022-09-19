from math import factorial


num=int(input("Enter a number : "))
factorial=1
for i in range(num,1,-1):
      factorial=factorial*i
print("Factorial is : ",factorial)      