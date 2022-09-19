num=int(input("Enter a number : "))
x=False
for i in range(2,num):
      if(num%i==0 ):
            x=True
            break
if(x==True):
            print("You number is not a prime number")
            
else:
            print ("Your number is  a prime number")