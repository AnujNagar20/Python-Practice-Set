def sum(n):
   
      if (n==1 or n==0 ):
            return 1
      
      return n+sum(n-1)    
f=sum(n=int(input("Enter the value of n = ")))           
print(f) 